import requests
import json
import pprint



salary_list_from = [] # список с зарплатами от...
salary_list_to = [] # список с зарплатами до...

for n in range(20):
    URL = 'https://api.hh.ru/vacancies'

    params = {'text': 'Python && Москва',
    'only_with_salary': True,
    'per_page': 100, 'page': n
    }

# {'id': '1', 'parent_id': '113', 'name': 'Москва', 'areas': []}

    result = requests.get(URL, params = params).json()

    for j in result['items']:
        # print(j['salary']['from'], j['salary']['to'])
        if j['salary']['from'] != None: # убираем зарплаты с пустным значением
            salary_list_from.append(j['salary']['from']) # создаем лист с зарплатой от...
        if j['salary']['to'] != None: # убираем зарплаты с пустным значением
            salary_list_to.append(j['salary']['to']) # создаем лист с зарплатой до...

print(salary_list_from, len(salary_list_from))
print(salary_list_to, len(salary_list_to))


# делим сумму списка зарплат от... на количество элементов списка
salary_from_average = sum(salary_list_from)/len(salary_list_from)
# делим сумму списка зарплат до... на количество элементов списка
salary_to_average = sum(salary_list_to)/len(salary_list_to)

print(f'Средняя зарплата: от {salary_from_average} до {salary_to_average}')

# Всего было найдено вакансий:
pprint.pprint(result['found'])