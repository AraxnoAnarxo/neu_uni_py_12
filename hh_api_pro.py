import requests
import pprint
import collections
import pymorphy2


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
            requirement.replace(",", " ").replace("—", " ").replace(".", " ")\
                          .replace("«", " ").replace("-", " ").replace("»", " ")\
                          .replace("(", " ").replace(")", " ").replace("!", " ")\
                          .replace("?", " ").replace(";", " ").replace(":", " ")
            requirement_list += requirement.split()
        except AttributeError:
            print('Error')

#print(requirement_list)

conjunctions = {"на", "не", "под", "у", "в", "с", "перед", "до", "о", "по", "из-за", "от", "для",
                "из-под", "над", "без", "близ", "ввиду", "между", "возле", "рядом", "около",
                "отношении", "вокруг", "впереди", "в продожение", "вследствие", "течение",
                "из", "кроме", "от", "подле", "по мере", "после", "прежде", "против",
                "благодаря", "вопреки", "к", "согласно", "соответсвенно", "несмотря",
                "про", "сквозь", "через", "во", "за", "об", "обо", "в", "соответствии",
                "надо", "перед", "согласно", "связи", "при", "без", "до", "для", "из",
                "под", "пред", "при", "ввиду", "насчет", "помощи", "случае", "условии",
                "погодя", "спустя", "благодаря", "начиная", "несмотря", "считая", "после",
                "мимо", "внутри", "вдоль", "вдали", "вокруг", "и", "или", "без", "можно"}

requirement_list_lower = list(map(lambda x: x.lower(), requirement_list))

#print(len(requirement_list_lower))
for i in requirement_list_lower:
    if i in conjunctions:
        requirement_list_lower.remove(i)



words0 = []
morph = pymorphy2.MorphAnalyzer()
for i in requirement_list_lower:
    words0.append(morph.parse(i)[0].normal_form)

words = dict()
c = collections.Counter(words0)
for key, value in c.items():
    words[key] = value

print(c.most_common(100))




