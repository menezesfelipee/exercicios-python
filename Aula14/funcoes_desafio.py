# DESAFIO - Data com mês por extenso.
# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.

# Modo 1 (NA RAÇA)

def converterDia(data):
    listaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    dia, mes, ano = data.split('/')
    listaCondicoes = [int(dia) < 1,
                      int(dia) > 31,
                      int(mes) in [3, 5, 8, 10] and int(dia) > 30,
                      int(ano) % 4 == 0 and int(mes) == 2 and int(dia) > 29,
                      int(ano) % 4 != 0 and int(mes) == 2 and int(dia) > 28]
    if  any(listaCondicoes):
        return 'A data não é válida.'
    else:
        return f'{dia} de {listaMeses[int(mes) - 1]} de {ano}'

data = input('Entre com a data no formato DD/MM/AAAA: ')
print(converterDia(data))


# Modo 2 (Biblioteca Datetime)

from datetime import datetime

def converterDia(data):
    listaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    dia, mes, ano = data.split('/')
    try:
        datetime(int(ano),int(mes),int(dia))
        return f'{dia} de {listaMeses[int(mes) - 1]} de {ano}'
    except ValueError:
        return 'A data não é válida.'

data = input('Entre com a data no formato DD/MM/AAAA: ')
print(converterDia(data))


# Modo 3 (Bibliotecas Datetime e Locale)

from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def converterDia(data):
    try:
        data = datetime.strptime(data, "%d/%m/%Y")
        return data.strftime("%d de %B de %Y")
    except ValueError:
        return 'A data não é válida.'

data = input('Entre com a data no formato DD/MM/AAAA: ')

print(converterDia(data))