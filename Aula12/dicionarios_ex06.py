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
        nota = round(uniform(0,10), 2)
        aluno['notas'].append(nota)
        media += (nota/5)
    aluno['media'] = round(media, 2)
    if aluno['media'] >= 7:
        aluno['situacao'] = 'aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situacao'] = 'recuperação'
    else:
        aluno['situacao'] = 'reprovado'
    classe.append(aluno)

print(f'{"Nome":>6} {"Notas":>37} {"Média":>30} {"Situação":>13}')

for aluno in classe:
    notas = '  -  '.join([f'{n:.2f}' for n in aluno['notas']])
    media = f"{aluno['media']:.2f}"
    print(f'{aluno["nome"]:<20} {notas:<48} {media:<10} {aluno["situacao"]}')