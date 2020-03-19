import requests
import pprint
import collections
import pymorphy2
import string


URL = 'https://api.hh.ru/vacancies'



requirement_list = []

for n in range(100):
    params = {'text': 'Python-разработчик', 'page': n}
    result = requests.get(URL, params=params).json()
    result_items = result['items']

    for i in result_items:
        result_snippet = i['snippet']
        requirement = result_snippet['requirement']
        try:
            # очистить текст c требованиями по вакансиям от знаков препинания и вставки "highlighttext". Убираем лишние пробелы
            for i in string.punctuation:
                requirement = requirement.replace(i, " ")
                requirement = requirement.replace('highlighttext', "")
                requirement = requirement.replace('   ', " ")
                requirement = requirement.replace('  ', " ")
            # requirement.replace(",", " ").replace("—", " ").replace(".", " ").replace(".", " ")\
            #               .replace("«", " ").replace("-", " ").replace("»", " ")\
            #               .replace("(", " ").replace(")", " ").replace("!", " ")\
            #               .replace("?", " ").replace(";", " ").replace(":", " ").replace("-", " ")
            requirement_list += requirement.split()
        except AttributeError:
            print(requirement)




other_words = {"работа","опыт", "работы","на", "не", "под", "у", "в", "с", "перед", "до", "о", "по", "из-за", "от", "для",
                "из-под", "над", "без", "близ", "ввиду", "между", "возле", "рядом", "около",
                "отношении", "вокруг", "впереди", "в продожение", "вследствие", "течение",
                "из", "кроме", "от", "подле", "по мере", "после", "прежде", "против",
                "благодаря", "вопреки", "к", "согласно", "соответсвенно", "несмотря",
                "про", "сквозь", "через", "во", "за", "об", "обо", "в", "соответствии",
                "надо", "перед", "согласно", "связи", "при", "без", "до", "для", "из",
                "под", "пред", "при", "ввиду", "насчет", "помощи", "случае", "условии",
                "погодя", "спустя", "благодаря", "начиная", "несмотря", "считая", "после",
                "мимо", "внутри", "вдоль", "вдали", "вокруг", "и", "или", "без", "можно", "лет", "уверенный",
               "опыт", "знание", "работа", "python", "разработка", "понимание", "experience", "умение", "python.",
               "хороший", "of", "язык", "in", "программирование", "and", "высокий", "with", "коммерческий", "3", "владение",
               "отличный", "python,", "/", "принцип", "работать", "1", "год", "менее", "один", "2-х","использование","технический",
               "<highlighttext>python</highlighttext>", "года", "knowledge", "2", "иметь", "быть", "база", "написание",
               "писать", "дать", "навык", "уровень", "образование", "years", "<highlighttext>development</highlighttext>", "с...",
               "и...", "3-х","промышленный","3","базовый","паттерн","желание","данных","образование","разработки.","реляционный","как",
               "структура","основный","система","код","strong","or","создание","современный","3.","good","проектирование","работы...'",
               "необходимый","+", "лет.", "-", "х", "c", "5", "приложение", "разработчик", "rest", "development", "web"}

requirement_list_lower = list(map(lambda x: x.lower(), requirement_list))
words0 = []
morph = pymorphy2.MorphAnalyzer()
for i in requirement_list_lower:
    words0.append(morph.parse(i)[0].normal_form)
# print(requirement_list_lower)
#print(len(requirement_list_lower))
# for i in other_words:
#     if i in words0:
#         words0.remove(i)

new_words = [word for word in words0 if word not in other_words]

# print(words0)



#3) получить из list пункта 3 dict, ключами которого являются слова,
# а значениями их количество появлений в тексте;



text_dict = {a: new_words.count(a) for a in new_words}
#print(text_dict)
# for keys, values in text_dict.items():
#     print(keys, values)
popular_words = []
for a in text_dict.values():
    popular_words.append(a)
popular_words.sort()

popular_10words = popular_words[-10:]

for keys, values in text_dict.items():
    if values in popular_10words:
        print(keys, values)

print()

# words = dict()
# c = collections.Counter(new_words)
# for key, value in c.items():
#     words[key] = value
#
# print(c.most_common(100))




