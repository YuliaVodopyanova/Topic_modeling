# import math
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# from collections import defaultdict
import os
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

# Пример коллекции новостных текстов
directory = "C:/Users/HP/Downloads/Telegram Desktop/data.zip"

for doc in os.listdir(directory):
    with open(directory+doc, 'r', encoding='utf-8') as f:
        tokens = f.read().split()
        for token in tokens:
            p = morph.parse(token)
            print(p)



#
# # Лемматизация текстов
# lemmatizer = WordNetLemmatizer()
# lemmatized_corpus = []
# for doc in corpus:
#     tokens = word_tokenize(doc.lower())
#     lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
#     lemmatized_corpus.append(lemmatized_tokens)
#
# # Подсчет IDF
# df = defaultdict(set)
# N = len(corpus)
# idf = {}
# for idx, tokens in enumerate(lemmatized_corpus):
#     unique_tokens = set(tokens)
#     for token in unique_tokens:
#         df[token].add(idx)
#
# for term in df:
#     idf[term] = math.log(N / len(df[term]))
#
# # Подсчет TF
# tf = defaultdict(dict)
# for idx, tokens in enumerate(lemmatized_corpus):
#     for token in tokens:
#         tf[token][idx] = 1 + math.log(tokens.count(token))
#
# # Обработка запроса и вычисление TF-IDF
# query = "first document"
# query_tokens = [lemmatizer.lemmatize(token) for token in word_tokenize(query.lower())]
# tfidf_scores = defaultdict(float)
# for term in query_tokens:
#     if term in tf:
#         for doc_idx in range(N):
#             tfidf_scores[doc_idx] += tf.get(term, {}).get(doc_idx, 0) * idf.get(term, 0)
#
# # Сортировка результатов по TF-IDF
# sorted_docs = sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)
# print(sorted_docs)