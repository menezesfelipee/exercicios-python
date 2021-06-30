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
        Aproveitamento: {self.golsPartida:.2f}'''

def menu():
    nome = input('Digite o nome do jogador: ')
    partidas = int(input('Digite a quantidade de partidas jogadas: '))
    golsTotal = int(input('Digite a quantidade de gols: '))
    return nome, partidas, golsTotal

jogadores = {}

while True:
    jogador = Jogador(menu())
    print(jogador.aproveitamento())
    continuar = input('Quer continuar cadastrando? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
    