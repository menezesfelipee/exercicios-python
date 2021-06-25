# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def iguais(n1, n2):
    if n1 < n2:
        return f'O menor é {n1}'
    elif n2 < n1:
        return f'O menor é {n2}'
    else:
        return 'Os números são iguais'

n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))

print(iguais(n1, n2))