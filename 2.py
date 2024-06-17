text = 'Мама мыла раму. Мама мыла раму? Мама мыла раму! "Мама мыла раму?" "Нет, не мыла!" "А зря". ' \
       'Мама мыла т.н. раму. Мама мыла... раму. Мама мыла раму для сестры, т.е. Нюры. Мама мыла раму для... Нюры. ' \
       'Мама мыла раму, поговорив с И.А. Крыловым. Мама мыла раму, поговорив с И. А. Крыловым. А.Б.В. Иванов. ' \
       'Мама мыла раму, поговорив с И. Крыловым. "И.А. Крылов расскажет басни". "И. Крылов расскажет басни". ' \
       '«Правда?» НЕКОТОРЫЕ ЛЮБЯТ КРИЧАТЬ. Т.к. Мила мыла раму, рама теперь чистая. Какое-то время назад. 1. ' \
       'Первое предложение. 2. Второе предложение. 1812 год был трудным для России. ' \
       'Это предложение не оканчивается точкой'


def get_sentences(text):
    sentences = []
    sentence = ""
    for id, char in enumerate(text):
        sentence += char
        if (char == '.' and text[id - 1].isdigit()) \
                or (char == '.' and text[id - 1].isupper() and (text[id - 2] == ' ' or text[id - 2] == '"')) \
                or (char == '.' and text[id-2] == '.'):
            continue
        elif char in ('.', '!', '?') and text[id + 1] == ' ':
            sentences.append(sentence.strip())
            sentence = ""
        elif char in ('"', '»') and text[id - 1] in (".", "!", "?"):
            sentences.append(sentence.strip())
            sentence = ""
    if sentence:
        sentences.append(sentence.strip())
    return sentences


for i in get_sentences(text):
    print(i)
