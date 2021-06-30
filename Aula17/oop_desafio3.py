class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, anos):
        if self.idade < 21:
            if self.idade + anos < 21:
                self.altura += anos*(0.5)
            else:
                self.altura += (21 - self.idade)*0.5
            self.idade += anos
        return f'Altura:{self.altura}\nIdade: {self.idade}'

pessoa1 = Pessoa('Felipe', 18, 60, 160)

print(pessoa1.envelhecer(50))