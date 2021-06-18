from random import sample
quantJogos = int(input('Quantos jogos você quer gerar? '))
todosJogos = []
for i in range(quantJogos):
    jogo = (sample(range(1,60), 6))
    if jogo.sort() not in todosJogos:
        todosJogos.append(jogo)
print('\nSeus jogos são:')
for a in range(quantJogos):
     print(todosJogos[a])
