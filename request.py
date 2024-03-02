import requests
from inputTreatment import IsCnpjValid
def RequestCnpj(cnpj):
    cnpj = IsCnpjValid(cnpj)
    if(cnpj):
        try:
            r = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj}')
            result = r.json()
            if(not isRequestValid):
                print("STATUS 200: BUSCA REALIZADA COM SUCESSO\n\n")
                print(result)
                print(result['status'])
            else:
                print(f"ERRO DE REQUISIÇÃO. CNPJ NÃO ENCONTRADO")
        except:
            print(f"ERRO {r.status_code}. A BUSCA NÃO PODE SER FEITA")
def isRequestValid(result):
    return result['status'] == 'ERROR'