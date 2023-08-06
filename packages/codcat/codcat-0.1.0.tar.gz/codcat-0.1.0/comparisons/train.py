import time
import warnings
from collections import defaultdict
from itertools import chain

from lightgbm import LGBMClassifier
from nltk import (
    TweetTokenizer,
    word_tokenize,
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import (
    CountVectorizer,
    HashingVectorizer,
    TfidfVectorizer,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from tqdm.auto import tqdm
from xgboost import XGBClassifier

from comparisons.nn import SimpleTransformersWrapper
from comparisons.tools import (
    FastTextVectorizer,
    SentenceTransformerVectorizer,
)

estimators = {}


warnings.simplefilter("ignore")


estimators["fasttext-lgbm"] = Pipeline(
    [
        (
            "fasttext-vectorizer",
            FastTextVectorizer(
                model_path="../notebooks/fasttext-embeddings.bin"
            ),
        ),
        ("lgbm", LGBMClassifier(n_jobs=-1, random_state=42)),
    ]
)
sentence_tr_models = [
    "multi-qa-mpnet-base-dot-v1",
    "all-distilroberta-v1",
    "all-MiniLM-L6-v2",
]
for model in sentence_tr_models:
    estimators[f"st-{model}-lgbm"] = Pipeline(
        [
            (
                "sentence-transformer-vectorizer",
                SentenceTransformerVectorizer(model_name_or_path=model),
            ),
            ("lgbm", LGBMClassifier()),
        ]
    )
estimators["tfidf-mnb-classic"] = Pipeline(
    [
        ("tfidf", TfidfVectorizer(tokenizer=word_tokenize)),
        ("mnb", MultinomialNB()),
    ]
)
estimators["tfidf-rf-word-tokenize"] = Pipeline(
    [
        ("tfidf", TfidfVectorizer(tokenizer=word_tokenize)),
        ("mnb", RandomForestClassifier(n_jobs=-1, random_state=42)),
    ]
)
estimators["tfidf-rf-tweet"] = Pipeline(
    [
        ("tfidf", TfidfVectorizer(tokenizer=TweetTokenizer().tokenize)),
        ("rf", RandomForestClassifier(n_jobs=-1, random_state=42)),
    ]
)
estimators["bow-lr"] = Pipeline(
    [
        (
            "count-vectorizer",
            CountVectorizer(tokenizer=TweetTokenizer().tokenize),
        ),
        ("lr", LogisticRegression()),
    ]
)
estimators["bow-rf"] = Pipeline(
    [
        (
            "count-vectorizer",
            CountVectorizer(tokenizer=TweetTokenizer().tokenize),
        ),
        ("rf", RandomForestClassifier(n_jobs=-1, random_state=42)),
    ]
)
estimators["bow-nb"] = Pipeline(
    [
        (
            "count-vectorizer",
            CountVectorizer(tokenizer=TweetTokenizer().tokenize),
        ),
        ("nb", MultinomialNB()),
    ]
)
estimators["tfidf-lr"] = Pipeline(
    [
        (
            "tfidf-vectorizer",
            TfidfVectorizer(tokenizer=TweetTokenizer().tokenize),
        ),
        ("lr", LogisticRegression()),
    ]
)
estimators["tfidf-xgboost"] = Pipeline(
    [
        ("tfidf-vectorizer", TfidfVectorizer(tokenizer=word_tokenize)),
        ("rf", XGBClassifier()),
    ]
)
estimators["tfidf-svm"] = Pipeline(
    [("tfidf-vectorizer", TfidfVectorizer(tokenizer=str.split)), ("svm", SVC())]
)
estimators["tfidf-lgbm"] = Pipeline(
    [
        (
            "tfidf-vectorizer",
            TfidfVectorizer(tokenizer=TweetTokenizer().tokenize),
        ),
        ("lgbm", LGBMClassifier(n_jobs=-1, random_state=42)),
    ]
)
estimators["hashing-lgbm"] = Pipeline(
    [
        ("hashing-vectorizer", HashingVectorizer(tokenizer=str.split)),
        ("rf", LGBMClassifier(n_jobs=-1, random_state=42)),
    ]
)
estimators["codebert"] = Pipeline(
    [
        (
            "codebert",
            SimpleTransformersWrapper("roberta", "microsoft/codebert-base"),
        ),
    ]
)
estimators["roberta"] = Pipeline(
    [
        (
            "roberta",
            SimpleTransformersWrapper(
                "roberta", "roberta-roberta-base-outputs"
            ),
        ),
    ]
)


def main(X_train, y_train, X_test, y_test, *datasets):
    results = defaultdict(dict)
    le = LabelEncoder()
    y_train_labeled = le.fit_transform(y_train)

    pbar = tqdm(estimators.items())

    try:
        for name, estimator in pbar:
            pbar.set_description("Fitting %s" % name)
            estimator.fit(X_train, y_train_labeled)
            for dataset_name, X, L in chain([("", X_test, y_test)], datasets):
                encoded_L = le.transform(L)
                start = time.time()
                y_pred = estimator.predict(X)
                results[name]["time-1sample"] = (time.time() - start) / len(X)
                f1 = f1_score(encoded_L, y_pred, average="macro")
                accuracy = accuracy_score(encoded_L, y_pred)
                precision = precision_score(
                    encoded_L, y_pred, average="weighted"
                )
                recall = recall_score(encoded_L, y_pred, average="weighted")

                postfix = f"-{dataset_name}" if dataset_name else ""
                results[name][f"f1{postfix}"] = f1
                results[name][f"accuracy{postfix}"] = accuracy
                results[name][f"precision{postfix}"] = precision
                results[name][f"recall{postfix}"] = recall
                results[name][
                    f"classification-report{postfix}"
                ] = classification_report(encoded_L, y_pred, output_dict=True)

                print("-" * 80)
                print(name)
                print(classification_report(encoded_L, y_pred))
                print("-" * 80)
    except Exception as e:
        print(e)

    return results


if __name__ == "__main__":
    import pandas as pd
    from sklearn.model_selection import train_test_split

    # train = pd.read_csv('../notebooks/train.csv')
    # test = pd.read_csv('../notebooks/test.csv')
    train = pd.read_json("../notebooks/train-code25.json")
    test = pd.read_json("../notebooks/test-code25.json")

    # test = pd.read_csv('../notebooks/test-preprocessed.csv')
    # train, test = train_test_split(train, random_state=42)
    X_train, y_train = train["code"], train["language"]
    X_test, y_test = test["code"], test["language"]

    # code25_train = pd.read_csv('../notebooks/train-preprocessed.csv')
    # code25_test = pd.read_csv('../notebooks/test-preprocessed.csv')
    # df = pd.read_csv('../notebooks/train-tiny.csv')
    # X_train, X_test, y_train, y_test = train_test_split(df['code'], df['language'], random_state=42)
    results = main(X_train, y_train, X_test, y_test)
    print(results)
    import json

    with open("results-code25-full.json", "w") as f:
        f.write(json.dumps(results, indent=4))
