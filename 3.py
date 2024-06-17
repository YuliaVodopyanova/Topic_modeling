from string import punctuation
import string


def get_words(text):
    new = ""
    for i in text:
        if i not in ('.', ',', '"', '\n'):
            new += i
    return [i for i in new.split(' ') if i]
    # result = text.split(' ')

    #     print(i)
    # return [i for i in result if i not in (punctuation, '\n')]


def get_counts(tokens):
    token_counts = {}

    for token in tokens:
        if token in token_counts:
            token_counts[token] += 1
        else:
            token_counts[token] = 1

    return token_counts


def get_edits_1(word):
    edits = set()
    # одна буква удалена
    for i in range(len(word)):
        edits.add(word[:i] + word[i+1:])
    #две соседние буквы меняются местами
    for i in range(len(word) - 1):
        edits.add(word[:i] + word[i+1] + word[i] + word[i+2:])
    #одна буква заменена на любую другую (из алфавита)
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            edits.add(word[:i] + letter + word[i+1:])
    #в начале, конце или между двумя соседними буквами вставлена буква из алфавита
    for i in range(len(word) + 1):
        for letter in string.ascii_lowercase:
            edits.add(word[:i] + letter + word[i:])
    return edits


def get_most_likely(word, frequencies):
    # if word in frequencies:
    #     return word

    transformations = get_edits_1(word)
    max_frequency = 0
    most_likely_word = word

    for transformation in transformations:
        if transformation in frequencies and frequencies[transformation] > max_frequency:
            max_frequency = frequencies[transformation]
            most_likely_word = transformation

    return most_likely_word


text = """The Fulton County Grand Jury said Friday an investigation of Atlanta 's recent primary election produced " no evidence " that any irregularities took place . 
The jury further said in term-end presentments that the City Executive Committee , which had over-all charge of the election , " deserves the praise and thanks of the City of Atlanta " for the manner in which the election was conducted . 
"""

# print(get_words(text))
# # print(get_counts(get_words(text)))
# print(get_edits_1("cat"))
# print(get_most_likely('in', get_counts(get_words(text))))
c = 0
lst = [['слушай', '.', 'не', 'терпи', 'алкоголик', '.', 'я', 'в', 'детство', 'настрадаться', 'из', '-', 'за', 'это', '.', 'мой', 'батя', 'запойный', 'быть', '.', 'вспоминать', 'он', 'абьюз', 'по', 'синька', ',', 'да', 'и', 'по', 'трезвянке', 'тоже', '.', 'до', 'сей', 'пора', 'трясти'], ['ок', 'пон', ',', 'это', 'абьюз', 'все', 'же', '.'], ['я', 'где', '-', 'то', 'читать', ',', 'что', 'систематическе', 'нарушение', 'сон', 'партнёр', '-', 'это', 'абьюз', '.', 'сейчас', 'весь', 'абьюз', ',', 'конечно', ',', 'но', 'как', 'же', 'неприятный', '.']]
for i in lst:
    # for n in i:
    c += i.count('абьюз')

# print(c)


def get_edit_distance(x, y):
    x = " " + x
    y = " " + y
    m = len(x)
    n = len(y)
    accum = {}

    def _d(i, j):
        if (i, j) in accum:
            return accum[(i, j)]

        if i < 0 and j < 0:
            return 0
        if i < 0:
            return j
        if j < 0:
            return i

        cost = 0 if x[i] == y[j] else 1
        result = min(_d(i-1, j) + 1, _d(i, j-1) + 1, _d(i-1, j-1) + cost)
        accum[(i, j)] = result
        return result

    for i in range(m):
        for j in range(n):
            _d(i, j)

    return _d(m - 1, n - 1)


