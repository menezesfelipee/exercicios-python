#03 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:
   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso

lista = []
maior = menor = 0
while True:
    pessoa = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    lista.append([pessoa, peso])
    continuar = input('\nVocê quer cadastrar mais pessoas? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Comando inválido. Você quer cadastrar mais pessoas? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
for i in lista:
    if i[1] >= maior:
        maior = i[1]
    if i[1] < menor or menor == 0:
        menor = i[1]
print(f'''Foram cadastradas {len(lista)} pessoas.
O maior peso cadastrado foi {maior} kg.
O menor peso cadastrado foi {menor} kg.''')
