# Adivinhe o Número

from time import sleep
from random import randint
numComp = randint(0, 20)
print('Olá, eu sou o computador e vou pensar num número de 0 a 20. Você pode adivinhar?\nEstou pensando num número', end='')
for a in '...........................':
    print(a, end = '', flush=True)
    sleep(0.2)
print('\n\nPronto! Pensei!\nAgora é a sua vez de palpitar.\n')
numUser = int(input ('Escolha um número de 0 a 20: '))
cont = 0
while True:
    cont += 1
    if numUser == numComp:
        break
    print('Você errou!')
    if numUser > numComp:
        print (f'O número que pensei é menor que {numUser}\n')
    else:
        print(f'O número que pensei é maior que {numUser}\n')
    numUser = int(input('Escolha outro número de 0 a 20: '))
print(f'Parabéns, você acertou o número que pensei ({numComp}) em {cont} palpites.')