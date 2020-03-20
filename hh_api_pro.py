import requests
import pprint
import collections
import pymorphy2
import string


def hh_requirements():
    URL = 'https://api.hh.ru/vacancies'



    requirement_list = []

    for n in range(100):
        params = {'text': 'Python-разработчик', 'page': n}
        result = requests.get(URL, params=params).json()
        result_items = result['items']
        results_all = result['found']

        for i in result_items:
            if i['snippet'] != None:  # убираем snippet с пустным значением
                result_snippet = i['snippet']
                if result_snippet['requirement'] != None:  # убираем requirement с пустным значением
                    requirement = result_snippet['requirement']

                    # очистить текст c требованиями по вакансиям от знаков препинания и вставки "highlighttext". Убираем лишние пробелы
                    for i in string.punctuation:
                        requirement = requirement.replace(i, " ")
                        requirement = requirement.replace('highlighttext', "")
                        requirement = requirement.replace('   ', " ")
                        requirement = requirement.replace('  ', " ")
                requirement_list += requirement.split()


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
    words_lemmed = []
    morph = pymorphy2.MorphAnalyzer()
    for i in requirement_list_lower:
        words_lemmed.append(morph.parse(i)[0].normal_form)


    new_words = [word for word in words_lemmed if word not in other_words]

    # c = collections.Counter()
    # for i in new_words:
    #     c[i] +=1


    c = collections.Counter(new_words)

    results = c.most_common(10)
    results_list = []

    for tuple_ in results:
        for i in range(len(tuple_)+1):
            if i == 0:
                results_list.append(tuple_[i])


    return results_all, results_list


a, b = hh_requirements()

print(a, b)
