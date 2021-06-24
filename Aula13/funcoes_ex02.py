# Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def valor(v):
    if v > 0:
        return 'P'
    else:
        return 'N'

n = int(input('Digite um número: '))

print(f'O valor {n} digitado é: {valor(n)}')