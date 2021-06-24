listaPar = []
listaImpar = []
lista = []
while True:
    num = int(input('\nDigite um número: '))
    if num % 2 == 0:
        listaPar.append(num)
        lista.append(num)
    else:
        listaImpar.append(num)
        lista.append(num)
    continuar = input('Você quer continuar cadastrando números? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Você quer continuar cadastrando números? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'''
Lista total:       {lista}
Lista dos pares:   {listaPar}
Lista dos Ímpares: {listaImpar}''')
