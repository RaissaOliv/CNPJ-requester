import re

def ReplaceInCnpj(cnpj) -> str:
    cnpj = re.sub('[^0-9]', '', cnpj)
    return cnpj

def IsCnpjValid(cnpj):
    cnpj = ReplaceInCnpj(cnpj)
    if(len(cnpj) == 14):
        cnpj = int(cnpj)
        return cnpj
    else:
        print("Cnpj inválido! O valor correto são 14 dígitos.")
        return False
