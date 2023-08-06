import os
import json
import argparse
from functools import partial
from multiprocessing import Pool  # 多线程并行
import tqdm
import torch
import pickle
import torch.nn.functional as F
from nltk import ngrams
from collections import Counter
import math
import random

# mutil-GPU
from torch.nn.parallel import DistributedDataParallel as DDP
import torch.distributed as dist

from transformers import HfArgumentParser
from transformers import AutoTokenizer, LlamaTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM, LlamaForCausalLM

from unilm import UniLMTokenizer, UniLMForConditionalGeneration

from arguments import parse_args

# Load and return model and tokenzier
def load_model(args):
    # Load corresponding model and tokenizer according to  model name ot path
    if args.is_seq2seq_model:
        tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(args.model_name_or_path)
    elif args.is_decoder_only_model:
        tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
        model = AutoModelForCausalLM.from_pretrained(args.model_name_or_path)
    elif args.is_llama:
        tokenizer = LlamaTokenizer.from_pretrained(args.model_name_or_path)
        model = LlamaForCausalLM.from_pretrained(args.model_name_or_path, torch_dtype=torch.float16)
    elif args.is_unilm:
        tokenizer = UniLMTokenizer.from_pretrained(args.model_name_or_path)
        model = UniLMForConditionalGeneration.from_pretrained(args.model_name_or_path)
    else:
        raise ValueError(f"Unknown model type: {args.model_name_or_path}")

    if args.use_gpu:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = model.to(device)
    else:
        device = "cpu"

    return tokenizer, model, device

# Generate text according to prompt and model
def generate(input, args, tokenizer, model, device):
    gen_kwargs = dict(max_new_tokens=args.max_new_tokens)
    if args.use_sampling:
        gen_kwargs.update(dict(
            do_sample=True,
            top_k=0,
            temperature=args.sampling_temp
        ))
    else:
        gen_kwargs.update(dict(
            num_beams=args.n_beams
        ))
    model = model.to(device)
    # generation function
    generate = partial(model.generate, **gen_kwargs)

    # restrict the length of input
    if args.prompt_max_length:
        pass
    elif hasattr(model.config, "max_position_embedding"):
        args.prompt_max_length = model.config.max_position_embeddings - args.max_new_tokens
    else:
        args.prompt_max_length = 2048 - args.max_new_tokens

    tokd_input = tokenizer(input, return_tensors="pt", add_special_tokens=True, truncation=True,
                           max_length=args.prompt_max_length).to(device)

    torch.manual_seed(args.generation_seed)
    output = generate(**tokd_input)

    # need to isolate the newly generated tokens
    output = output[:, tokd_input["input_ids"].shape[-1]:]

    decoded_output_text = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

    return decoded_output_text

# Used to count the top k n-grams  in a given text set
def count_n_grams(text_set, n, top_k, tokenizer):
    n_grams = []
    for text in text_set:
        text_n_grams = ngrams(tokenizer.convert_tokens_to_ids(tokenizer.tokenize(text)), n)
        n_grams.extend(text_n_grams)

    # Count and sort(according to value in dict, return key) n-grams，
    n_grams = sorted(Counter(n_grams), reverse=True)

    if len(n_grams) < top_k:
        return n_grams
    else:
        return n_grams[:top_k]

def next_token_probs(n_grams, top_k, model, tokenizer, device):
    grams_probs = {}
    for i in tqdm.tqdm(range(len(n_grams))):
        prompt = tokenizer.decode(n_grams[i])
        tokd_input = tokenizer.encode(prompt, return_tensors="pt").to(device)

        model.to(device)
        with torch.no_grad():
            outputs = model(tokd_input)
            predictions = outputs[0]

        logits = predictions[0, -1, :]

        # probability
        probs = F.softmax(logits, dim=0)

        values, indices = torch.topk(probs, top_k, -1)
        indices = indices.tolist()
        values = values.tolist()
        grams_probs[str(n_grams[i])] = dict(zip(indices, values))

    return grams_probs

# construct test text set with original text set and generated test set
def construct_test_text_set(original_text_set, generated_test_set, args):
    test_set = []
    for i in generated_test_set:
        if i != "":
            test_set.append({"text": i, "label": args.model_name})
    test_set.extend(original_text_set)
    random.shuffle(test_set)
    return test_set

# Calculate proxy perplexity according to n-grams probability
def proxy_perplexity(text_tokenize_ids, args, probability_2_grams, probability_3_grams, probability_4_grams, probability_5_grams):
    test_ppl = []
    # Calculate proxy perplexity
    for j in tqdm.tqdm(range(len(text_tokenize_ids))):
        for label, tokenize_ids in text_tokenize_ids[j].items():
            ppl_result = {}
            # ppl = math.log2(probability_2_grams[tokenize_ids[0]][str(tokenize_ids[1])])
            ppl = 0
            number_5_grams = 0
            number_4_grams = 0
            number_3_grams = 0
            number_2_grams = 0
            for i in range(3, len(tokenize_ids)-1):

                # 5-grams proxy perplexity
                if str([tokenize_ids[i - j] for j in range(3, -1, -1)]) in probability_5_grams.keys():
                    if str(tokenize_ids[i + 1]) in probability_5_grams[str([tokenize_ids[i - j] for j in range(3, -1, -1)])].keys():
                        ppl = ppl + math.log2(probability_5_grams[str([tokenize_ids[i - j] for j in range(3, -1, -1)])][str(tokenize_ids[i + 1])])
                    else:
                        top_k = len(probability_5_grams[str([tokenize_ids[i - j] for j in range(3, -1, -1)])].keys())
                        sum_probs = sum(probability_5_grams[str([tokenize_ids[i - j] for j in range(3, -1, -1)])].values())
                        if (1 - sum_probs) > 0:
                            ppl = ppl + math.log2((1 - sum_probs) / (args.vocab_length - top_k))
                    number_5_grams = number_5_grams + 1

                # 4-grams proxy perplexity
                elif str([tokenize_ids[i - j] for j in range(2, -1, -1)]) in probability_4_grams.keys():
                    if str(tokenize_ids[i + 1]) in probability_4_grams[str([tokenize_ids[i - j] for j in range(2, -1, -1)])].keys():
                        ppl = ppl + math.log2(probability_4_grams[str([tokenize_ids[i - j] for j in range(2, -1, -1)])][str(tokenize_ids[i + 1])])
                    else:
                        top_k = len(probability_4_grams[str([tokenize_ids[i - j] for j in range(2, -1, -1)])].keys())
                        sum_probs = sum(probability_4_grams[str([tokenize_ids[i - j] for j in range(2, -1, -1)])].values())
                        if (1 - sum_probs) > 0:
                            ppl = ppl + math.log2((1 - sum_probs) / (args.vocab_length - top_k))
                    number_4_grams = number_4_grams + 1

                # 3-grams proxy perplexity
                elif str([tokenize_ids[i - 1], tokenize_ids[i]]) in probability_3_grams.keys():
                    if str(tokenize_ids[i + 1]) in probability_3_grams[str([tokenize_ids[i - 1], tokenize_ids[i]])].keys():
                        ppl = ppl + math.log2(probability_3_grams[str([tokenize_ids[i - 1], tokenize_ids[i]])][str(tokenize_ids[i + 1])])
                    else:
                        top_k = len(probability_3_grams[str([tokenize_ids[i - 1], tokenize_ids[i]])].keys())
                        sum_probs = sum(probability_3_grams[str([tokenize_ids[i - 1], tokenize_ids[i]])].values())
                        if (1 - sum_probs) > 0:
                            ppl = ppl + math.log2((1 - sum_probs) / (args.vocab_length - top_k))
                    number_3_grams = number_3_grams + 1

                # 2-grams proxy perplexity
                elif str([tokenize_ids[i]]) in probability_2_grams.keys():
                    if str(tokenize_ids[i+1]) in probability_2_grams[str([tokenize_ids[i]])].keys():
                        ppl = ppl + math.log2(probability_2_grams[str([tokenize_ids[i]])][str(tokenize_ids[i+1])])
                    else:
                        top_k = len(probability_2_grams[str([tokenize_ids[i]])].keys())
                        sum_probs = sum(probability_2_grams[str([tokenize_ids[i]])].values())
                        ppl = ppl + math.log2((1-sum_probs) / (args.vocab_length - top_k))
                    number_2_grams = number_2_grams + 1
            ppl = round(ppl / (number_2_grams + number_3_grams + number_4_grams + number_5_grams + 1), 2)
            ppl_result[label] = -ppl
            test_ppl.append(ppl_result)
    return test_ppl

def main(args):
    args.is_seq2seq_model = any([(model_type in args.model_name_or_path) for model_type in ["t5", "T0"]])
    args.is_decoder_only_model = any([(model_type in args.model_name_or_path) for model_type in ["gpt", "opt", "bloom"]])
    args.is_gpt = any([(model_type in args.model_name_or_path) for model_type in ["gpt"]])
    args.is_opt = any([(model_type in args.model_name_or_path) for model_type in ["opt"]])
    args.is_unilm = any([(model_type in args.model_name_or_path) for model_type in ["unilm"]])
    args.is_llama = any([(model_type in args.model_name_or_path) for model_type in ["llama"]])

    if args.is_gpt:
        args.model_name = "gpt"
        args.vocab_length = 50257
    elif args.is_opt:
        args.model_name = "opt"
        args.vocab_length = 50265
    elif args.is_unilm:
        args.model_name = "unilm"
        args.vocab_length = 28996
    elif args.is_llama:
        args.model_name = "llama"
        args.vocab_length = 32000

    if args.prompt_file is not None:
        extension = args.prompt_file.split(".")[-1]
        assert extension in ["csv", "json", "tsv"], "`prompt_file` should be a csv or a json file."

    # load prompt set
    prompt = []
    with open(args.prompt_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                text = json.loads(line)
                prompt.append(text)

            except Exception as e:
                print(e, line)

    # load model and tokenizer
    torch.cuda.set_device(args.local_rank)
    dist.init_process_group(backend='nccl')
    tokenizer, model, device = load_model(args)
    model = DDP(model)

    generate_fn = partial(generate, args=args, tokenizer=tokenizer, model=model, device=device)
    generation_text = []

    # check if there is a saved state
    if args.save_state:
        try:
            with open(args.save_state, 'rb') as f:
                state = pickle.load(f)
                generation_text = state['generation_text']
                start_batch = state['start_batch']

        except Exception as e:
            print(e)

    else:
        start_batch = 0

    for batch in tqdm.tqdm(range(start_batch, args.n_generate_text // (args.batch_size * dist.get_world_size()))):
        input = prompt[batch * args.batch_size * dist.get_world_size():(batch + 1) * args.batch_size * dist.get_world_size()]
        for idx in range(len(input)):
            generation_text.append(generate_fn(input[idx]))

        # save state after each batch
        if args.save_state:
            state = {
                "generateion_text": generation_text,
                "state_batch": batch - 1
            }
            with open(args.save_state, "wb") as f:
                pickle.dump(state, f)

    out_dir = os.path.join("result", args.model_name)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    generation_text_file = os.path.join(out_dir, args.generated_text_file)
    with open(generation_text_file, "w", encoding='utf-8') as f:
        for text in generation_text:
            f.write(json.dumps(text, ensure_ascii=False))
            f.write('\n')

    # save final state
    if args.save_state:
        state = {
            'generation_text': generation_text,
            'start_batch': args.n_generate_text // args.batch_size,
        }
        with open(args.save_state, 'wb') as f:
            pickle.dump(state, f)

    statistics_text_set = generation_text[:int(args.n_generate_text * 0.8)]
    generation_test_text_set = generation_text[int(args.n_generate_text * 0.8):args.n_generate_text]

    # count the number of n-grams
    one_grams = count_n_grams(statistics_text_set, 1, args.n_one_grams, tokenizer)
    two_grams = count_n_grams(statistics_text_set, 2, args.n_two_grams, tokenizer)
    three_grams = count_n_grams(statistics_text_set, 3, args.n_three_grams, tokenizer)
    four_grams = count_n_grams(statistics_text_set, 4, args.n_four_grams, tokenizer)

    # samples the next token probability of n-grams
    two_grams_probs = next_token_probs(one_grams, args.two_grams_top_k, model, tokenizer, device)
    three_grams_probs = next_token_probs(two_grams, args.three_grams_top_k, model, tokenizer, device)
    four_grams_probs = next_token_probs(three_grams, args.four_grams_top_k, model, tokenizer, device)
    five_grams_probs = next_token_probs(four_grams, args.five_grams_top_k, model, tokenizer, device)

    two_grams_probs_file = os.path.join(out_dir, args.two_grams_probs_file)
    with open(two_grams_probs_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(two_grams_probs, ensure_ascii=False))

    three_grams_probs_file = os.path.join(out_dir, args.three_grams_probs_file)
    with open(three_grams_probs_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(three_grams_probs, ensure_ascii=False))

    four_grams_probs_file = os.path.join(out_dir, args.four_grams_probs_file)
    with open(four_grams_probs_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(four_grams_probs, ensure_ascii=False))

    five_grams_probs_file = os.path.join(out_dir, args.five_grams_probs_file)
    with open(five_grams_probs_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(five_grams_probs, ensure_ascii=False))

    original_text_set = []
    with open(args.original_test_file, 'r', encoding="utf-8") as f:
        for line in f:
            try:
                text = json.loads(line)
                original_text_set.append(text)
            except Exception as e:
                print(e, line)

    test_set = construct_test_text_set(original_text_set, generation_test_text_set, args)

    new_test_file = os.path.join(out_dir, args.new_test_file)
    with open(new_test_file, "w", encoding='utf-8') as f:
        for text in test_set:
            f.write(json.dumps(text, ensure_ascii=False))
            f.write('\n')

    test_text_tokenize_ids = []
    for i in tqdm.tqdm(range(len(test_set))):
        tokenize_ids = {}
        if args.is_gpt:
            text_tokenize = tokenizer.tokenize(test_set[i]["text"], truncation=True)
        else:
            text_tokenize = tokenizer.tokenize(test_set[i]["text"])
        tokenize_ids[text[i]["label"]] = tokenizer.convert_tokens_to_ids(text_tokenize)
        # tokens to token_ids
        test_text_tokenize_ids.append(tokenize_ids)

    test_ppl = proxy_perplexity(test_text_tokenize_ids, args, two_grams_probs, three_grams_probs, four_grams_probs, five_grams_probs)

    test_ppl_file = os.path.join(out_dir, args.test_ppl_file)
    with open(test_ppl_file, "w", encoding='utf-8') as f:
        for ppl in test_ppl:
            f.write(json.dumps(ppl, ensure_ascii=False))
            f.write('\n')



if __name__ == "__main__":
    args = parse_args()
    # print(args)
    main()

