from Parser import TarifCalculation
import requests
requestUrl = "https://my-json-server.typicode.com/kelrus/TestTaskQA/db"

def emulation_request(request):

    data = requests.get(url = requestUrl).json()

    result = {
        "result": 500
    }

    tarifs = []
    for item in data:
        tarifs.append(item)

    tarif = request['city']
    sum = request['sum']

    if TarifCalculation.is_tariff_exists(tarif, tarifs):
        plusKoff = data[tarif]['plus_koff']
        multiplicationKoff = data[tarif]['multiplication_koff']
        divisionKoff = data[tarif]['division_koff']
        result["result"] = TarifCalculation.tarif_calc(sum, plusKoff, multiplicationKoff, divisionKoff)
    else:
        plusKoff = data['based']['plus_koff']
        multiplicationKoff = data['based']['multiplication_koff']
        divisionKoff = data['based']['division_koff']
        result["result"] = TarifCalculation.tarif_calc(sum, plusKoff, multiplicationKoff, divisionKoff)

    return result

