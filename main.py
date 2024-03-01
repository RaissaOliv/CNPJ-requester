from request import RequestCnpj
if __name__ == '__main__':
        cnpj = (input("Bem vindo!\n\nDigite o cnpj que deseja buscar: "))
        RequestCnpj(cnpj)

#inputs de teste: 
    # cnpj válido (não int): 17.895.646/0001-87
    # cnpj válido (int): 17895646000187
    # cnpj inválido (digitei qualquer coisa): 06123787217222 
    # cnpj inválido (maior que 14, não int): 17.895.646/0001-877
    # cnpj inválido(maior que 14, int): 178956460001877
    # cnpj inválido(menor que 14, não int): 17.895.646/0001-8
    # cnpj inválido(menor que 14, int): 1789564600018