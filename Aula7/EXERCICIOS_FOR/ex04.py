soma = cont = 0
for c in range(6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma dos {cont} números pares foi de {soma}.')