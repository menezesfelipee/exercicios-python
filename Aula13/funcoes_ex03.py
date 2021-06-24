# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.

# Modo 1
def soma(nota1 = 0, nota2 = 0, nota3 = 0):
    return nota1 + nota2 + nota3

def media(soma):
    return f'{soma/3:.2f}'

n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
n3 = float(input('Digite o 3º valor: '))

print(f'A soma é igual a {soma(n1, n2, n3)} e a média dos três valores é igual a {media(soma(n1, n2, n3))}')


# Modo 2
def soma(n1 = 0, n2 = 0, n3 = 0):
    return n1 + n2 + n3

def media(soma):
    return f'{soma / 3:.2f}'

def menu():
    n1 = float(input('Digite o 1º valor: '))
    n2 = float(input('Digite o 2º valor: '))
    n3 = float(input('Digite o 3º valor: '))
    print(f'A soma é {soma(n1, n2, n3)} e a média é {media(soma(n1, n2, n3))}.')

menu()