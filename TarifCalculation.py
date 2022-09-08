

def tarif_calc(sum, plus_koff, multiplication_koff, division_koff):
    result = sum + plus_koff + multiplication_koff * division_koff
    return result

requestUrl = "https://my-json-server.typicode.com/kelrus/TestTaskQA/db"

def is_tariff_exists(tarif, tarifs):
    for item in tarifs:
        if tarif == item:
            return True
    return False