# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado. Não esqueça que os lançamentos são feitos de forma randômica.

from random import randint, choice

class Lancador:
    def __init__(self):
        self.moeda = choice(['Cara', 'Coroa'])
        self.dado = randint(1, 6)
    def jogar(self, opcao):
        if opcao == 'M':
            return self.moeda
        elif opcao == 'D':
            return self.dado
        else:
            return 'Opção inválida'

moeda1 = Lancador()
opcao = input('Você quer sortear moeda ou dado? [M/D] ').strip().upper()[0]
print(f'A moeda caiu em: {moeda1.jogar(opcao)}')

dado1 = Lancador()
opcao = input('Você quer sortear moeda ou dado? [M/D] ').strip().upper()[0]
print(f'O dado caiu em: {dado1.jogar(opcao)}')
