'''02 - Aprimore o desafio anterior, mostrando no final:
   A) A soma de todos os valores pares digitados.
   B) A soma dos valores da terceira coluna. 
   C) O maior valor da segunda linha.'''

matriz = []
somaPar = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor da {i+1}ª linha e {j+1}ª coluna: '))
        linha.append(valor)
        if valor % 2 == 0:
            somaPar += valor
    matriz.append(linha)
print(f'''\nA soma de todos os valores pares é de {somaPar}.
A soma dos valores da terceira coluna é de {sum(matriz[2])}.
O maior valor da segunda linha é {max(matriz[1])}.''')
