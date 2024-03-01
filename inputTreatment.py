import re
    
def IsCnpjTooBig(cnpj) -> bool:
    return (len(str(cnpj)) > 18)

def IsCnpjTooSmall(cnpj) -> bool:
    return (14 > len(cnpj))

def ReplaceInCnpj(cnpj) -> str:
    cnpj = re.sub('[^0-9]', '', cnpj)
    return cnpj

def IsCnpjValid(cnpj):
    if(not IsCnpjTooBig(cnpj)):
       cnpj = ReplaceInCnpj(cnpj)
    else:
        print("Cnpj inválido! Tamanho excede o limite. O valor correto são 14 números.")
        return False
    
    if(not IsCnpjTooSmall(cnpj) and not IsCnpjTooBig(cnpj)):
        cnpj = int(cnpj)
        return cnpj
    else:
        print("Cnpj inválido! O valor correto são 14 dígitos.")
        return False
