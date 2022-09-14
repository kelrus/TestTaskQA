
def tarif_calc(sum, plusKoff, multiplicationKoff, divisionKoff):
    result = round(sum + plusKoff + multiplicationKoff * divisionKoff, 2)
    return result

requestUrl = "https://my-json-server.typicode.com/kelrus/TestTaskQA/db"

def is_tariff_exists(tarif, tarifs):
    for item in tarifs:
        if tarif == item:
            return True
    return False