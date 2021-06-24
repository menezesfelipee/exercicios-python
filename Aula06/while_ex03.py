# Jogo de Par ou Ímpar

from random import randint
vitorias = 0
while True:
    numComp = randint(0,10)
    escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]
    while escolha not in 'PI':
        escolha = input('Escolha corretamente: Par ou Ímpar? [P/I]: ').strip().upper()[0]
    numUser = int(input('Escolha um número de 0 a 10: '))
    soma = numComp + numUser
    if escolha == 'P':
        if soma % 2 == 0:
            vitorias += 1
            print(f'O computador escolheu {numComp} e o total foi {soma}.\nVocê ganhou! Vamos jogar novamente!\n')
        else:
            break
    if escolha == 'I':
        if soma % 2 != 0:
            vitorias += 1
            print(f'O computador escolheu {numComp} e o total foi {soma}.\nVocê ganhou! Vamos jogar novamente!\n')
        else:
            break
print(f'O computador escolheu {numComp} e o total foi {soma}.\n\nGame Over!\nVocê teve {vitorias} vitórias!')