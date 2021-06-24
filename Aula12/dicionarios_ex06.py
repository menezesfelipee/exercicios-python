'''6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as situações dos 15 alunos de uma vez só.'''

from random import uniform
from names import get_first_name

classe = list()

for i in range(15):
    aluno = dict()
    aluno['nome'] = get_first_name()
    aluno['notas'] = list()
    media = 0
    for j in range(5):
        nota = round(uniform(0,10), 2)     # 'uniform' sorteia um ponto flutuante no intervalo dado, inclusive o limite superior e inferior  ||  'round' arrendoda para a quantidade de casas decimais dada
        aluno['notas'].append(nota)
        media += (nota/5)                  # (nota1 + nota2 + nota3 + nota4 + nota5) / 5   =   (nota1 / 5) + (nota2 / 5) + (nota3 / 5) + (nota4 / 5) + (nota5 / 5)
    aluno['media'] = round(media, 2)       # Já a arredonda a média para a 2 casas decimais
    if aluno['media'] >= 7:
        aluno['situacao'] = 'aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situacao'] = 'recuperação'
    else:
        aluno['situacao'] = 'reprovado'
    classe.append(aluno)

## PARA FORMATAR A F-STRING PODEMOS UTILIZAR OS SÍMBOLOS A SEGUIR: ##
# >6  : vai guardar exatamente 6 espaços para caracteres para a sua coluna, alinhando À DIREITA.
# <20 : vai guardar exatamente 20 espaços para caracteres para a sua coluna, alinhando À ESQUERDA.
# ^10 : vai guardar exatamente 10 espaços para caracteres para a sua coluna, alinhando AO CENTRO.
# .2f : coloca exatamente 2 casas decimais no float, preenchendo com zeros, se necessário

## VOCÊ PODE MISTURAR A FORMATAÇÃO DE ESPAÇOS E DE CASAS DECIMAIS ##
# <15.3f : vai guardar exatamente 15 espaços para caracteres para a sua coluna, alinhando À ESQUERDA, e coloca exatamente 3 casas decimais no float

print('┏', '━'*15, '┳', '━'*44, '┳', '━'*9, '┳', '━'*14, '┓', sep='')
print(f'┃{"Nome":^15}┃{"Notas":^44}┃{"Média":^9}┃{"Situação":^14}┃')
print('┣', '━'*15, '╋', '━'*44, '╋', '━'*9, '╋', '━'*14, '┫', sep='')

for aluno in classe:
    notas = ' -  '.join([f'{n:<5.2f}' for n in aluno['notas']])
    print(f'┃{aluno["nome"]:<15}┃{notas:^44}┃{aluno["media"]:<9.2f}┃{aluno["situacao"]:<14}┃')

print('┗', '━'*15, '┻', '━'*44, '┻', '━'*9, '┻', '━'*14, '┛', sep='')