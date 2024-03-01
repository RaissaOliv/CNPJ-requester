import requests
from inputTreatment import IsCnpjValid
def RequestCnpj(cnpj):
    cnpj = IsCnpjValid(cnpj)
    if(cnpj):
        r = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj}')
        if(r.status_code == 200):
            print("STATUS 200: BUSCA REALIZADA COM SUCESSO\n\n")
            print(r.text)
        else:
            raise Exception(f"ERRO {r.status_code}. A BUSCA NÃO PODE SER FEITA")
