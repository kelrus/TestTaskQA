import TarifCalculation
import json



def generator_test_cases():
    with open('json/db.json', 'r', encoding='utf8') as readfile:
        data = json.load(readfile)

    cases = {}
    cases['cases'] = []
    tarifs = get_tarifs(data)
    sum = 10000

    for tarif in data:
        expectedResult = res_generation_function(tarif, sum, TarifCalculation.is_tariff_exists(tarif, tarifs), data)
        request  = req_generation_function(tarif, sum)
        testCase = (request, expectedResult)
        cases['cases'].append(testCase)

    with open('json/TestCases.json', 'w', encoding='utf8') as outfile:
        json.dump(cases, outfile, indent=2, ensure_ascii=False)


def req_generation_function(city, sum):
    request = {
        "city": city,
        "sum": sum
    }
    return request

def res_generation_function(tarif, sum, isExists, data):

    result = {
        "result": 500
    }

    if isExists:
        plus_koff = data[tarif]['plus_koff']
        multiplication_koff = data[tarif]['multiplication_koff']
        division_koff = data[tarif]['division_koff']
        result["result"] = TarifCalculation.tarif_calc(sum, plus_koff, multiplication_koff, division_koff)
    else:
        plus_koff = data['based']['plus_koff']
        multiplication_koff = data['based']['multiplication_koff']
        division_koff = data['based']['division_koff']
        result["result"] = TarifCalculation.tarif_calc(sum, plus_koff, multiplication_koff, division_koff)

    return result

def get_tarifs(data):
    tarifs = []
    for tarif in data:
        tarifs.append(tarif)
    return tarifs


def get_test_cases():
    generator_test_cases()

    with open('json/TestCases.json', 'r', encoding='utf8') as readfile:
        casesjson = json.load(readfile)

    testCases = []
    for case in casesjson['cases']:
        testCases.append(tuple(case))


    return testCases
