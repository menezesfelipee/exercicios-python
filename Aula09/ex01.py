lista = []
while True:
    num = int(input('\nDigite um número: '))
    if num not in lista:
        lista.append(num)
    continuar = input('Você quer continuar cadastrando números? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Você quer continuar cadastrando números? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'\n{sorted(lista)}')
