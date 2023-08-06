import numpy as np
import datasets
from tqdm import tqdm
import math
import json
from transformers import AutoTokenizer
from unilm import UniLMTokenizer
from lightgbm import Booster


def load_probability():
    dm = datasets.DownloadManager()
    files = dm.download_and_extract('https://huggingface.co/datasets/wukx/n-grams_sample_probability/resolve/main/new_n_grams.zip')
    n_grams = np.load(f'{files}/new_n_grams.npz' , allow_pickle=True)
    global gpt_n_grams_probability, opt_n_grams_probability, unilm_n_grams_probability
    gpt_n_grams_probability = n_grams["gpt"]
    opt_n_grams_probability = n_grams["opt"]
    unilm_n_grams_probability = n_grams["unilm"]

# Calculate the perplexity of text.
def perplexity(text_set_token_ids, n_grams_probability, vocab_size):

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
            if tuple([text_token_ids[i - j] for j in range(2, -1, -1)]) in n_grams_probability[4].keys():
                if text_token_ids[i + 1] in n_grams_probability[4][tuple([text_token_ids[i - j] for j in range(2, -1, -1)])]:
                    if n_grams_probability[5][tuple([text_token_ids[i - j] for j in range(2, -1, -1)])][n_grams_probability[4][tuple([text_token_ids[i - j] for j in range(2, -1, -1)])].tolist().index(text_token_ids[i + 1])] > 0:
                        ppl = ppl + math.log2(n_grams_probability[5][tuple([text_token_ids[i - j] for j in range(2, -1, -1)])][n_grams_probability[4][tuple([text_token_ids[i - j] for j in range(2, -1, -1)])].tolist().index(text_token_ids[i + 1])])
                else:
                    top_k = len(n_grams_probability[4][tuple([text_token_ids[i - j] for j in range(2, -1, -1)])])
                    sum_probs = sum(n_grams_probability[5][tuple([text_token_ids[i - j] for j in range(2, -1, -1)])])
                    if (1 - sum_probs) > 0:
                        ppl = ppl + math.log2((1 - sum_probs) / (vocab_size - top_k))
                number_4_grams = number_4_grams + 1

            # Calculate the perplexity with 3-grams samples probability
            elif tuple([text_token_ids[i - 1], text_token_ids[i]]) in n_grams_probability[2].keys():
                if text_token_ids[i + 1] in n_grams_probability[2][tuple([text_token_ids[i - 1], text_token_ids[i]])]:
                    if n_grams_probability[3][tuple([text_token_ids[i - 1], text_token_ids[i]])][n_grams_probability[2][tuple([text_token_ids[i - 1], text_token_ids[i]])].tolist().index(text_token_ids[i + 1])] > 0:
                        ppl = ppl + math.log2(
                            n_grams_probability[3][tuple([text_token_ids[i - 1], text_token_ids[i]])][n_grams_probability[2][tuple([text_token_ids[i - 1], text_token_ids[i]])].tolist().index(text_token_ids[i + 1])])
                else:
                    top_k = len(n_grams_probability[2][tuple([text_token_ids[i - 1], text_token_ids[i]])])
                    sum_probs = sum(n_grams_probability[3][tuple([text_token_ids[i - 1], text_token_ids[i]])])
                    if (1 - sum_probs) > 0:
                        ppl = ppl + math.log2((1 - sum_probs) / (vocab_size - top_k))
                number_3_grams = number_3_grams + 1

            # Calculate the perplexity with 2-grams samples probability
            elif tuple([text_token_ids[i]]) in n_grams_probability[0].keys():
                if text_token_ids[i + 1] in n_grams_probability[0][tuple([text_token_ids[i]])]:
                    if n_grams_probability[1][tuple([text_token_ids[i]])][n_grams_probability[0][tuple([text_token_ids[i]])].tolist().index(text_token_ids[i + 1])] > 0:
                        ppl = ppl + math.log2(n_grams_probability[1][tuple([text_token_ids[i]])][n_grams_probability[0][tuple([text_token_ids[i]])].tolist().index(text_token_ids[i + 1])])
                else:
                    top_k = len(n_grams_probability[0][tuple([text_token_ids[i]])])
                    sum_probs = sum(n_grams_probability[1][tuple([text_token_ids[i]])])
                    if (1 - sum_probs) > 0:
                        ppl = ppl + math.log2((1 - sum_probs) / (vocab_size - top_k))
                number_2_grams = number_2_grams + 1

        perplexity = round(ppl / (number_2_grams + number_3_grams + number_4_grams + 1), 2)
        test_perplexity.append(-perplexity)

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
    # files = dm.download_and_extract('https://huggingface.co/datasets/wukx/n-grams_sample_probability/resolve/main/n_grams.zip')

    model_information = [{"model_name": "gpt2", "vocab_size": 50265, "model_probability": "gpt_n_grams_probability"},
                         {"model_name": "facebook/opt-1.3b", "vocab_size": 50257, "model_probability": "opt_n_grams_probability"},
                         {"model_name": "microsoft/unilm-base-cased", "vocab_size": 28996, "model_probability": "unilm_n_grams_probability"}]

    # Calculate the proxy perplexity
    perplexity_result = []
    for model in model_information:
        if any([(model_type in model["model_name"]) for model_type in ["unilm"]]):
            tokenizer = UniLMTokenizer.from_pretrained(model["model_name"])
        else:
            tokenizer = AutoTokenizer.from_pretrained(model["model_name"])

        text_token_ids = []
        for text in test_text:
            if any([(model_type in model["model_name"]) for model_type in ["gpt"]]):
                text_tokenize = tokenizer.tokenize(text, truncation=True)
            else:
                text_tokenize = tokenizer.tokenize(text)
            text_token_ids.append(tokenizer.convert_tokens_to_ids(text_tokenize))


        if model["model_probability"] in globals():
            perplexity_result.append(perplexity(text_token_ids, globals()[model["model_probability"]], model["vocab_size"]))
        else:
            raise ValueError(
                "The {} does not exist, please load n-grams probability!".format(model["model_probability"])
            )

    # The input features of classiffier
    features = np.stack([perplexity_result[i] for i in range(len(perplexity_result))], axis=1)
    print(features)

    # Load classiffier model
    model_files = dm.download_and_extract(
        'https://huggingface.co/datasets/wukx/n-grams_sample_probability/resolve/main/LightGBM_model.zip')
    model = Booster(model_file=f'{model_files}/LightGBM_model.txt')
    y_pred = model.predict(features)
    label = ["Human_write", "GPT-2", "OPT", "UniLM"]
    test_result = [{label[i]: y_pred[j][i] for i in range(len(label))} for j in range(len(y_pred))]

    return test_result
