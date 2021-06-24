# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

from datetime import datetime

def voto(anoNasc):
    anoAtual = datetime.now().year
    if 18 <= anoAtual - anoNasc < 70:
        return 'OBRIGATÓRIO'
    elif anoAtual - anoNasc < 16:
        return 'NEGADO'
    else:
        return 'OPCIONAL'


ano = int(input('Digite o ano de nascimento: '))

print(f'Esse cidaão tem voto: {voto(ano)}')