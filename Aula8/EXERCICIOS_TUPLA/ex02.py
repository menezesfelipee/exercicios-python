tupla = (float(input('Digite o primeiro valor: ')),
float(input('Digite o segundo valor: ')),
float(input('Digite o terceiro valor: ')),
float(input('Digite o quarto valor: ')))
print(f'''
O número 9 apareceu {tupla.count(9)} vezes.
O primeiro valor 3 apareceu na posição [{tupla.index(3)}].''')