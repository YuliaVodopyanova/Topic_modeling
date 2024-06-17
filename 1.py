import re
from pymystem3 import Mystem

s = 'МУЗ-ТВ @muz_tv #МУЗКалендарь Сегодня празднует день рождения французская дива, песни которой покоряют сердца миллионов людей, Милен Фармер. ' \
    '#happybirthday Love Radio @LoveRadioRuВторой конкурсный день «Новой волны - 2017» http://www.loveradio.ru/new/93923.htm #LoveRadio #НоваяВолна'

hashtag = re.findall('#\w+|@\w+|http[s]*\S+', s)


s1 = 'В фильме снимались: Л. Мерзин, В. Титова, П. Якоби, У. Росберг, Т. Логинова, В. Басов и другие. ' \
     'В фильме снимались: О. Табаков, А. Миронов, С. Мишулин, Ю. Толубеев, Е. Евстигнеев, Витя Галкин и другие. ' \
     'В фильме снимались: Ира Волкова, Таня Невская, Сережа Кусков, Н. Гвоздикова, А. Харитонов, С. Котикова и другие.'

people = re.findall('[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+|[А-ЯЁ]\.\s[А-ЯЁ][а-яё]+', s1)

# print(people)

text = 'Мой дядя самых честных правил,' \
       'Когда не в шутку занемог,' \
       'Он уважать себя заставил ' \
       'И лучше выдумать не мог.'

lemma = Mystem().lemmatize(text)
print(lemma)
l = [i for i in lemma if i.isalpha()]
print(l)

analyzed = Mystem().analyze(text)
# print(analyzed)

# just_nouns = [x['text'] for x in analyzed if 'analysis' in x and x['analysis'][0]['gr'].startswith('S,')]
# print(just_nouns)

nouns_with_case = []
for word in analyzed:
    if 'analysis' in word and word['analysis'][0]['gr'].startswith('S,'):
        noun_info = word['analysis'][0]['gr'].split('=')[1].split(',')[0]
        nouns_with_case.append(f"{word['text'].lower()} - {noun_info}")
print(nouns_with_case)
