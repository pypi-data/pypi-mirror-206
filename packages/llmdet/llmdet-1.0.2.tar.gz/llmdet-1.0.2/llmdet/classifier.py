from lightgbm import LGBMClassifier, Booster
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score, f1_score, precision_recall_fscore_support
import json
import numpy as np

def construct_data(perplexity_file):
    perplexity = []
    label = []
    with open(perplexity_file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                for i, j in data.items():
                    perplexity.append(j)
                    if i == "human_write":
                        label.append(0)
                    elif i == "gpt2":
                        label.append(1)
                    elif i == "opt":
                        label.append(2)
                    elif i == "unilm":
                        label.append(3)
            except Exception as e:
                print(e, line)

    return perplexity, label

def LightGBM_Classification(X, y, n):
    # Load train dataset
    X = np.array(X)
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12343)

    model = LGBMClassifier(
        max_depth=3,
        learning_rate=0.1,
        n_estimators=200,
        objective='multiclass',
        num_class=n,
        booster='gbtree',
        min_child_weight=2,
        subsample=0.8,
        colsample_bytree=0.8,
        reg_alpha=0,
        reg_lambda=1,
        seed=0)

    model.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], verbose=100, early_stopping_rounds=50)

    # Save model
    model.booster_.save_model("LightGBM_model.txt")

    return X_test,  y_test

if __name__ == "__main__":
    GPT_perplexity, label_1 = construct_data("new_gpt_ppl.json")
    OPT_perplexity, label_2 = construct_data("new_opt_ppl.json")
    UniLM_perplexity, label_3 = construct_data("new_unilm_ppl.json")
    perplexity = [[i, j, k] for i, j, k in zip(GPT_perplexity, OPT_perplexity, UniLM_perplexity)]

    # Ground truth label
    ground_label = []
    for i, j, k in zip(label_1, label_2, label_3):
        if i == j and i == k and j == k:
            ground_label.append(i)

    # Train classification model and return test data
    X_test, y_test = LightGBM_Classification(perplexity, ground_label, 4)

    # Load trained model
    model = Booster(model_file='LightGBM_model.txt')
    # Make predictions on the test setMake predictions on the test set
    y_pred = model.predict(X_test)
    y_pred = [np.argmax(i) for i in y_pred]
    # Calculate accuracy, recall, f1 value
    p_class, r_class, f_class, support_micro = precision_recall_fscore_support(y_test, y_pred, labels=[i for i in range(4)])
    print(f_class)

