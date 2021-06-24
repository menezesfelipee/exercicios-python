# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

def voto(anoNasc):
    from datetime import datetime
    idade = datetime.now().year - anoNasc
    if 18 <= idade < 70:
        return 'OBRIGATÓRIO'
    elif idade < 16:
        return 'NEGADO'
    else:
        return 'OPCIONAL'

ano = int(input('Digite o ano de nascimento: '))

print(f'Para quem nasceu em {ano} o voto é {voto(ano)}')