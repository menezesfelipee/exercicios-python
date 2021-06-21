# Modo 1
from random import randint
quantJogos = int(input('Quantos jogos você quer gerar? '))
todosJogos = []
for i in range(quantJogos):
    jogo = []
    while True:
        numero = randint(1,60)
        if numero not in jogo:
            jogo.append(numero)
        if len(jogo) == 6:
            break
    jogo.sort()
    todosJogos.append(jogo)
print('\nSeus jogos são:')
for a in range(quantJogos):
     print(todosJogos[a])


# Modo 2
from random import sample
quantJogos = int(input('Quantos jogos você quer gerar? '))
todosJogos = []
for i in range(quantJogos):
    jogo = (sample(range(1,61), 6))
    jogo.sort()
    todosJogos.append(jogo)
print('\nSeus jogos são:')
for a in range(quantJogos):
     print(todosJogos[a])
