'''6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as situações dos 15 alunos de uma vez só.'''

classe = list()

for i in range(15):
    aluno = dict()
    aluno['nome'] = input('Digite o nome: ').capitalize()
    aluno['notas'] = list()
    media = 0
    for j in range(5):
        nota = float(input(f'Digite a {j+1}ª nota '))
        aluno['notas'].append(nota)
        media += nota/5
    aluno['media'] = round(media, 2)
    if aluno['media'] >= 7:
        aluno['situacao'] = 'aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situacao'] = 'recuperação'
    else:
        aluno['situacao'] = 'reprovado'
    classe.append(aluno)

print()

print(f'{"Nome":^25} {"Notas":^25} {"Média":^25} {"Situação":^25}')
for aluno in classe:
    notas = ", ".join([str(n) for n in aluno['notas']])
    print(f'{aluno["nome"]:^25} {notas:^25} {aluno["media"]:^25} {aluno["situacao"]:^25}')