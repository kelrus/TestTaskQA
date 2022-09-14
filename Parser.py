import TarifCalculation
import json
import random

minSum = 0
maxSum = 999999999
noTarifsCity = ['Aljir', 'паhyа', 'vdgddl', 'Город']

#функция для считывания тарифа из json файла,
#автоматического формирования тест-кейсов
#и записи их в файл json
def generator_test_cases():
    #Считываем тело json файла с тарифами
    with open('db.json', 'r', encoding='utf8') as readfile:
        data = json.load(readfile)


    cases = {}
    cases['cases'] = []

    #Существующие города с тарифами
    tarifs = get_tarifs(data)
    #Города для теста с тарифами и без
    cities = get_cities(tarifs)

    #Функция автоматического формирования тест-кейсов на основе json файла
    #Тест кейс - это структура запроса + ожидаемый результат.
    for tarif in cities:
        # Формируем запрос
        sum = round(random.uniform(minSum, maxSum), 2)
        request = req_generation_function(tarif, sum)

        #Получаем ожидаем результат для этого запроса
        expectedResult = res_generation_function(tarif, sum, TarifCalculation.is_tariff_exists(tarif, tarifs), data)
        testCase = (request, expectedResult)
        cases['cases'].append(testCase)


    #Запись получеенных тест-кейсов в json файл
    with open('json/TestCases.json', 'w', encoding='utf8') as outfile:
        json.dump(cases, outfile, indent=2, ensure_ascii=False)


#Функция получения списка всех гордов для тест кейса
#Получает на вход существующие города с тарифами, добавляет туда несуществующие тарифы и
#выдаёт полный список городов для формирования запросов
def get_cities(cities):
    new_cites = []

    for city in cities:
        new_cites.append(city)
    for city in noTarifsCity:
        new_cites.append(city)

    return new_cites

#Функцию формирования тела запроса на основе тарифа
def req_generation_function(city, sum):
    #тело запроса
    request = {
        "city": city,
        "sum": sum
    }
    return request


#Функцию формирования тела ответа на основе тарифа
def res_generation_function(tarif, sum, isExists, data):

    #тело ответа
    result = {
        "result": 500
    }

    #Проверка на существование тарифа. Если он он сущетсвует, то формируется ответ на основе этого тарифа.
    if isExists:
        #Данные тарифа для расчёта result
        plusKoff = data[tarif]['plus_koff']
        multiplicationKoff = data[tarif]['multiplication_koff']
        divisionKoff = data[tarif]['division_koff']
        #Поле result высчитывается из формулы TarifCalculation
        result["result"] = TarifCalculation.tarif_calc(sum, plusKoff, multiplicationKoff, divisionKoff)
    #Если не существует, то используется базовый тариф
    else:
        #Данные базового тарифа для расчёта result
        plusKoff = data['based']['plus_koff']
        multiplicationKoff = data['based']['multiplication_koff']
        divisionKoff = data['based']['division_koff']
        # Поле result высчитывается из формулы TarifCalculation
        result["result"] = TarifCalculation.tarif_calc(sum, plusKoff, multiplicationKoff, divisionKoff)

    return result

#Функция получения тарифов.
def get_tarifs(data):
    tarifs = []
    for tarif in data:
        tarifs.append(tarif)
    return tarifs

#Функция для получения тест кейсов и отправки их на тесты
def get_test_cases():

    with open('json/TestCases.json', 'r', encoding='utf8') as readfile:
        casesjson = json.load(readfile)

    testCases = []
    for case in casesjson['cases']:
        testCases.append(tuple(case))


    return testCases


#При запуске parser генерирует тест-кейсы
generator_test_cases()