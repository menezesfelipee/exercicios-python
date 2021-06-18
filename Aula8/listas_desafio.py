# Modo 1
perguntas = [input('Telefonou para a vítima? [S/N] ').strip().upper()[0],
input('Esteve no local do crime? [S/N] ').strip().upper()[0],
input('Mora perto da vítima? [S/N] ').strip().upper()[0],
input('Devia para a vítima? [S/N] ').strip().upper()[0],
input('Já trabalhou com a vítima? [S/N] ').strip().upper()[0]]
if perguntas.count('S') == 2:
    print('Suspeita')
elif perguntas.count('S') == 3 or perguntas.count('S') == 4:
    print('Cúmplice')
elif perguntas.count('S') == 5:
    print('Assassino')
else:
    print('Inocente')


# Modo 2
perguntas = [input('Telefonou para a vítima? [S/N] ').strip().upper()[0],
input('Esteve no local do crime? [S/N] ').strip().upper()[0],
input('Mora perto da vítima? [S/N] ').strip().upper()[0],
input('Devia para a vítima? [S/N] ').strip().upper()[0],
input('Já trabalhou com a vítima? [S/N] ').strip().upper()[0]]
respostas = ['Inocente','Suspeita','Cúmplice','Cúmplice','Assassino']
quant = perguntas.count('S') - 1
print(f'Você é {respostas[quant]}')


# Modo 3
perguntas = ['Telefonou para a vítima? [S/N] ',
'Esteve no local do crime? [S/N] ',
'Mora perto da vítima? [S/N] ',
'Devia para a vítima? [S/N] ',
'Já trabalhou com a vítima? [S/N] ']
for i in range(len(perguntas)):
    perguntas[i] = input(perguntas[i]).strip().upper()[0]
respostas = ['Inocente','Suspeita','Cúmplice','Cúmplice','Assassino']
print(f'Você é {respostas[perguntas.count("S") - 1]}')