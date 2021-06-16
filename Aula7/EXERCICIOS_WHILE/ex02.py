cont18 = contH = contM = 0
while True:
    idade = int(input('\nQual é a sua idade? '))
    sexo = input('Qual é o seu sexo? [M/F] ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Qual é o seu sexo? [M/F] ').strip().upper()[0]
    parar = input('\nVocê quer cadastrar mais pessoas? [S/N]: ').strip().upper()[0]
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        contH += 1
    if sexo == 'F' and idade < 20:
        contM +=1
    if parar == 'N':
        break
print(f'''
{cont18} pessoas têm mais de 18 anos.
{contH} pessoas são homens.
{contM} mulheres têm menos de 20 anos.
''')