from random import randint

class Lancador:
    def __init__(self):
        self.moeda = randint(0, 1)
        self.dado = randint(1,6)
    def jogarMoeda(self):
        if self.moeda == 0:
            self.moeda = 'Cara'
        else:
            self.moeda = 'Coroa'
        return self.moeda
    def jogarDado(self):
        return self.dado
        
sortear = Lancador()
print(sortear.jogarMoeda())
print()
print(sortear.jogarDado())
