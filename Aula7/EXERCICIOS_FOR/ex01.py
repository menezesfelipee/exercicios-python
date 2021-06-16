# Modo 1

p = float(input(f'Digite seu peso 1 em kg: '))
menor = maior = p
for a in range(2,6):
    p = float(input(f'Digite o peso {a} em kg: '))
    if menor > p:
        menor = p
    if p > maior:
        maior = p
print(f'O menor peso é {menor:.2f}kg e o maior é {maior:2f}kg.')

# Modo 2

menor = maior = 0
for a in range(1,6):
    p = float(input(f'Digite o peso {a} em kg: '))
    if menor > p or menor == 0:
        menor = p
    if p > maior:
        maior = p
print(f'O menor peso é {menor:.2f}kg e o maior é {maior:.2f}kg.')