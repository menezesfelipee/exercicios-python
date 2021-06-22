# 1.    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import datetime
anoAtual = datetime.now().year
pessoa = dict()
pessoa['nome'] = input('Digite seu nome: ')
pessoa['anoNascimento'] = int(input('Digite seu ano de nascimento: '))
pessoa['idade'] = anoAtual - pessoa['anoNascimento']
pessoa['ctps'] = input('Digite sua Carteira de Trabalho, se não possuir digite 0: ')
if pessoa['ctps'] != 0:
    pessoa['anoContratacao'] = int(input('Digite o ano que você foi contratado: '))
    pessoa['idadeAposentadoria'] =  pessoa['anoContratacao'] + 35 - pessoa['anoNascimento']
    pessoa['salario'] = float(input('Digite seu salário: '))
print(f'''
{pessoa["nome"]} tem {pessoa["idade"]} anos e vai se aposentar com {pessoa["idadeAposentadoria"]} anos.
''')
