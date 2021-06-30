# Vamos aprimorar o código: cadastro de jogador de futebol.py que foi desenvolvido no CodeLab da aula14. Faça com que o seu código funcione para vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

# Modo 1

class Jogador:
    def __init__(self, nome, partidas, golsTotal):
        self.nome = nome
        self.partidas = partidas
        self.golsTotal = golsTotal
        self.golsPartida = self.golsTotal / self.partidas
    def aproveitamento(self):
        return f'''
        Nome: {self.nome}
        Partidas: {self.partidas}
        Gols no Campeonato: {self.golsTotal}
        Aproveitamento: {self.golsPartida:.2f} por partida'''

def menu():
    nome = input('Digite o nome do jogador: ')
    partidas = int(input('Digite a quantidade de partidas jogadas: '))
    golsTotal = int(input('Digite a quantidade de gols: '))
    return Jogador(nome, partidas, golsTotal)

time = dict()

while True:
    jogador = menu()
    time[jogador.nome] = jogador
    print(jogador.aproveitamento())
    continuar = input('Quer continuar cadastrando? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print(time['felipe'].aproveitamento())


# Modo 2

class Jogador:
    def __init__(self):
        self.nome = input('Digite o nome do jogador: ')
        self.partidas = int(input('Digite a quantidade de partidas jogadas: '))
        self.golsTotal = int(input('Digite a quantidade de gols: '))
        self.golsPartida = self.golsTotal / self.partidas
    def aproveitamento(self):
        return f'''
        Nome: {self.nome}
        Partidas: {self.partidas}
        Gols no Campeonato: {self.golsTotal}
        Aproveitamento: {self.golsPartida:.2f} por partida'''

time = dict()

while True:
    jogador = Jogador()
    time[jogador.nome] = jogador
    print(jogador.aproveitamento())
    continuar = input('Quer continuar cadastrando? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print(time['felipe'].aproveitamento())