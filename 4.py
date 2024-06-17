# import re
#
# def tokenize(text):
#     return re.findall(r'[\w+]', text)
#     # return text.split()
#
# t = 'jfnv, kgmb krejgtv. kmejrg.'
# print(tokenize(t))
#
#
# def get_ngram_counts(words, n):
#     ngrams = {}
#     for i in range(len(words) - n + 1):
#         ngram = tuple(words[i:i+n])
#         ngrams[ngram] = ngrams.get(ngram, 0) + 1
#     return ngrams
#
#
# def train_language_model(corpus, n):
#     tokens = tokenize(corpus)
#     ngrams = get_ngram_counts(tokens, n)
#     return ngrams
#
#
# def get_prob(text, ngrams, n, corp_size):
#     tokens = tokenize(text)
#     prob = 1.0
#     for i in range(len(tokens) - n + 1):
#         ngram = tuple(tokens[i:i+n])
#         count = ngrams.get(ngram, 0)
#         prob *= (count + 1) / (corp_size + len(ngrams))
#     return prob
#
#
# corpus = 'I saw a cat and a dog. The cat was sleeping, and the dog was awake. I woke up the cat.'
# words = tokenize(corpus)
# corp_size = len(words)
# ngrams = get_ngram_counts(words, 2)
# tests = ('a cat', 'the cat', 'the dog', 'the woke', 'the cat was awake')
# for t in tests:
#     print(t, get_prob(t, ngrams, 2, corp_size))


import re
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
# import nltk


# with open("C:/Users/HP/Downloads/Telegram Desktop/neg_train.txt", "r", encoding="utf-8") as f:
#     # negative_corpora = re.split(r'\n+', f.read().strip())
#     neg_text = f.read()
#
# neg_reviews = neg_text.split('\n\n')


with open("C:/Users/HP/Downloads/Telegram Desktop/features.txt") as f:
    features = f.readlines()
    # features = [defaultdict(int) for i in range(2)]
        #re.split(r'\n+', f.read().strip())
    # classes = [0, 1]

with open("C:/Users/HP/Downloads/Telegram Desktop/pos_train.txt") as f:
    # positive_corpora = re.split(r'\n+', f.read().strip())
    pos_text = f.read()

pos_reviews = pos_text.split('\n\n')


def extract_features(text, features):
    # words = word_tokenize(text.lower())

    words = text.lower().split()
    res = []
    # features[word] += 1
    for f in features:
        res.append(words.count(f))
    return res


def train_nbc(features, classes, corpora):
    total = sum(features.values())
    priors = defaultdict(float)
    params = defaultdict(lambda: defaultdict(float))

    for idx, corpus in enumerate(corpora):
        for text in corpus:
            extract_features(text, features[idx])
        for word, count in features[idx].items():
            params[word][idx] = count / total
        priors[idx] = len(corpus) / total

    return priors, params


def classify(text, features, classes, priors, params):
    words = word_tokenize(text)
    scores = defaultdict(float)

    for idx in classes:
        scores[idx] = priors[idx]
        for word in words:
            scores[idx] *= params.get(word, {}).get(idx, 1e-6)

    pred_class = max(scores, key=scores.get)
    return pred_class


# if __name__ == "__main__":

# with open("C:/Users/HP/Downloads/Telegram Desktop/neg_train.txt", "r", encoding="utf-8") as f:
#     # negative_corpora = re.split(r'\n+', f.read().strip())
#     negative_corpora = f.read()
#
# with open("C:/Users/HP/Downloads/Telegram Desktop/features.txt", "r", encoding="utf-8") as f:
#     features = f.read()
#         #re.split(r'\n+', f.read().strip())
#     classes = [0, 1]
#
# with open("C:/Users/HP/Downloads/Telegram Desktop/pos_train.txt", "r", encoding="utf-8") as f:
#     # positive_corpora = re.split(r'\n+', f.read().strip())
#     positive_corpora = f.read()
#
# pos_reviews = pos_text.split('\n\n')

print(extract_features(pos_reviews[0], features))

    # priors, params = train_nbc(features, classes, [positive_corpora, negative_corpora])
    #
    # test_text = "The movie was awful"
    # pred_class = classify(test_text, features, classes, priors, params)
    # if pred_class == 0:
    #     print("The review is positive.")
    # else:
    #     print("The review is negative.")

