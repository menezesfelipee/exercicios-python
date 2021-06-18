total = cont = 0
produtoMaisBarato = nome = input('Qual é o nome do produto que você quer cadastrar? ')
valorMaisBarato = valor = float(input('Qual é o valor desse produto? '))
while True:
    total += valor
    if valor > 1000:
        cont += 1
    if valor <= valorMaisBarato:
        produtoMaisBarato = nome
        valorMaisBarato = valor
    parar = input('\nVocê quer cadastrar mais itens? [S/N] ').strip().upper()[0]
    while parar not in 'SN':
        parar = input('Você quer cadastrar mais itens? [S/N] ').strip().upper()[0]
    if parar == 'N':
        break
    nome = input('\nQual é o nome do produto que você quer cadastrar? ')
    valor = float(input('Qual é o valor desse produto? '))
print(f'''
O total gasto foi de R$ {total:.2f}
{cont} produtos custam mais de R$ 1000,00
{produtoMaisBarato} é o produto mais barato.''')