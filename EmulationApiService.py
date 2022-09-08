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

