''' 01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:

[  1  ][  2  ][  3  ]
[  4  ][  5  ][  6  ]
[  7  ][  8  ][  9  ] 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''

# Modo 1
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor da {i+1}ª linha e {j+1}ª coluna: '))
        linha.append(valor)
    matriz.append(linha)
print('\nA matriz declarada foi:\n')
for a in matriz:
    print(f'    [ {a[0]} ]   [ {a[1]} ]   [ {a[2]} ]')
    

# Modo 2
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor da {i+1}ª linha e {j+1}ª coluna: '))
        linha.append(valor)
    matriz.append(linha)
print('\nA matriz declarada foi:')
for i in matriz:
    print()
    for j in i:
        print(f'    [ {j} ]', end='')