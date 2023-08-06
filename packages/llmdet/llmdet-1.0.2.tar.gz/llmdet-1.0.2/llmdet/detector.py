import numpy as np
import datasets
from tqdm import tqdm
import math
import json
from transformers import AutoTokenizer
from unilm import UniLMTokenizer
from lightgbm import Booster


# Calculate the perplexity of text.
def perplexity(text_set_token_ids, n_grams_probability, vocab_size):
    # Load n-grams probability
    probability_2_grams_keys = n_grams_probability['sample_probs'][0]["keys"]
    probability_2_grams_values = n_grams_probability['sample_probs'][0]["values"]
    probability_3_grams_keys = n_grams_probability['sample_probs'][1]["keys"]
    probability_3_grams_values = n_grams_probability['sample_probs'][1]["values"]
    probability_4_grams_keys = n_grams_probability['sample_probs'][2]["keys"]
    probability_4_grams_values = n_grams_probability['sample_probs'][2]["values"]

    # Calculate proxy perplexity value for test text set
    test_perplexity = []

    for k in tqdm(range(len(text_set_token_ids))):
        text_token_ids = text_set_token_ids[k]
        ppl = 0
        number_3_grams = 0
        number_4_grams = 0
        number_2_grams = 0
        for i in range(2, len(text_token_ids) - 1):

            # Calculate the perplexity with 4-grams samples probability
            if tuple([text_token_ids[i - j] for j in range(2, -1, -1)]) in probability_4_grams_keys.keys():
                if text_token_ids[i + 1] in probability_4_grams_keys[tuple([text_token_ids[i - j] for j in range(2, -1, -1)])]:
                    if probability_4_grams_values[tuple([text_token_ids[i - j] for j in range(2, -1, -1)])][probability_4_grams_keys[tuple([text_token_ids[i - j] for j in range(2, -1, -1)])].tolist().index(text_token_ids[i + 1])] > 0:
                        ppl = ppl + math.log2(probability_4_grams_values[tuple([text_token_ids[i - j] for j in range(2, -1, -1)])][probability_4_grams_keys[tuple([text_token_ids[i - j] for j in range(2, -1, -1)])].tolist().index(text_token_ids[i + 1])])
                else:
                    top_k = len(probability_4_grams_keys[tuple([text_token_ids[i - j] for j in range(2, -1, -1)])])
                    sum_probs = sum(probability_4_grams_values[tuple([text_token_ids[i - j] for j in range(2, -1, -1)])])
                    if (1 - sum_probs) > 0:
                        ppl = ppl + math.log2((1 - sum_probs) / (vocab_size - top_k))
                number_4_grams = number_4_grams + 1

            # Calculate the perplexity with 3-grams samples probability
            elif tuple([text_token_ids[i - 1], text_token_ids[i]]) in probability_3_grams_keys.keys():
                if text_token_ids[i + 1] in probability_3_grams_keys[tuple([text_token_ids[i - 1], text_token_ids[i]])]:
                    if probability_3_grams_values[tuple([text_token_ids[i - 1], text_token_ids[i]])][probability_3_grams_keys[tuple([text_token_ids[i - 1], text_token_ids[i]])].tolist().index(text_token_ids[i + 1])] > 0:
                        ppl = ppl + math.log2(probability_3_grams_values[tuple([text_token_ids[i - 1], text_token_ids[i]])][probability_3_grams_keys[tuple([text_token_ids[i - 1], text_token_ids[i]])].tolist().index(text_token_ids[i + 1])])
                else:
                    top_k = len(probability_3_grams_keys[tuple([text_token_ids[i - 1], text_token_ids[i]])])
                    sum_probs = sum(probability_3_grams_values[tuple([text_token_ids[i - 1], text_token_ids[i]])])
                    if (1 - sum_probs) > 0:
                        ppl = ppl + math.log2((1 - sum_probs) / (vocab_size - top_k))
                number_3_grams = number_3_grams + 1

            # Calculate the perplexity with 2-grams samples probability
            elif tuple([text_token_ids[i]]) in probability_2_grams_keys.keys():
                if text_token_ids[i + 1] in probability_2_grams_keys[tuple([text_token_ids[i]])]:
                    if probability_2_grams_values[tuple([text_token_ids[i]])][probability_2_grams_keys[tuple([text_token_ids[i]])].tolist().index(text_token_ids[i + 1])] > 0:
                        ppl = ppl + math.log2(probability_2_grams_values[tuple([text_token_ids[i]])][probability_2_grams_keys[tuple([text_token_ids[i]])].tolist().index(text_token_ids[i + 1])])
                else:
                    top_k = len(probability_2_grams_keys[tuple([text_token_ids[i]])])
                    sum_probs = sum(probability_2_grams_values[tuple([text_token_ids[i]])])
                    if (1 - sum_probs) > 0:
                        ppl = ppl + math.log2((1 - sum_probs) / (vocab_size - top_k))
                number_2_grams = number_2_grams + 1

        perplexity = round(ppl / (number_2_grams + number_3_grams + number_4_grams + 1), 2)
        test_perplexity.append(perplexity)

    return test_perplexity

# Detect function
def detect(text):
    # Determine whether the input is a single text or a collection of text.
    if isinstance(text, str):
        test_text = [text]
    elif isinstance(text, list):
        if isinstance(text[0], str):
            test_text = text
        else:
            raise ValueError(
                "The type of `text` which you input is not a string or list. "
                "Please enter the correct data type for `text`."
            )
    else:
        raise ValueError(
            "The type of `text` which you input is not a string or list. "
            "Please enter the correct data type for `text`."
        )
    dm = datasets.DownloadManager()
    files = dm.download_and_extract('https://huggingface.co/datasets/wukx/n-grams_sample_probability/resolve/main/n_grams.zip')
        
    gpt_tokenizer = AutoTokenizer.from_pretrained("gpt2")
    gpt_vocab_size = 50265
    text_gpt_token_ids = []
    for text in test_text:
        gpt_text_tokenize = gpt_tokenizer.tokenize(text, truncation=True)
        text_gpt_token_ids.append(gpt_tokenizer.convert_tokens_to_ids(gpt_text_tokenize))
    gpt_sample_probability_file = f'{files}/n_grams/gpt.npz'
    # Load GPT model's n-grams probability data
    gpt_n_grams_probability = np.load(gpt_sample_probability_file, allow_pickle=True)
    gpt_perplexity = perplexity(text_gpt_token_ids, gpt_n_grams_probability, gpt_vocab_size)

    opt_tokenizer = AutoTokenizer.from_pretrained("facebook/opt-1.3b")
    opt_vocab_size = 50257
    text_opt_token_ids = []
    for text in test_text:
        opt_text_tokenize = opt_tokenizer.tokenize(text)
        text_opt_token_ids.append(opt_tokenizer.convert_tokens_to_ids(opt_text_tokenize))
    opt_sample_probability_file = f'{files}/n_grams/opt.npz'
    # Load OPT model's n-grams probability data
    opt_n_grams_probability = np.load(opt_sample_probability_file, allow_pickle=True)
    opt_perplexity = perplexity(text_opt_token_ids, opt_n_grams_probability, opt_vocab_size)

    unilm_tokenizer = UniLMTokenizer.from_pretrained("microsoft/unilm-base-cased")
    unilm_vocab_size = 28996
    text_unilm_token_ids = []
    for text in test_text:
        unilm_text_tokenize = unilm_tokenizer.tokenize(text)
        text_unilm_token_ids.append(unilm_tokenizer.convert_tokens_to_ids(unilm_text_tokenize))
    unilm_sample_probability_file = f'{files}/n_grams/unilm.npz'
    # Load UniLM model's n-grams probability data
    unilm_n_grams_probability = np.load(unilm_sample_probability_file, allow_pickle=True)
    unilm_perplexity = perplexity(text_unilm_token_ids, unilm_n_grams_probability, unilm_vocab_size)

    # Load classiffier model
    model_files = dm.download_and_extract('https://huggingface.co/datasets/wukx/n-grams_sample_probability/resolve/main/LightGBM_model.zip')
    model = Booster(model_file=f'{model_files}/LightGBM_model.txt')
    test_result = []
    for gpt, opt, unilm in zip(gpt_perplexity, opt_perplexity, unilm_perplexity):
        y_pred = model.predict([[gpt, opt, unilm]])
        result = {"Human_write": y_pred[0][0], "GPT-2": y_pred[0][1], "OPT": y_pred[0][2], "UniLM": y_pred[0][3]}
        test_result.append(result)
    return test_result
