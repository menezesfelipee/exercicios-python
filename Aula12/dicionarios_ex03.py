'''3. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.'''

aluno = dict()

aluno['nome'] = input('Digite o nome do aluno: ').strip().capitalize()
aluno['media'] = float(input(f'Digite a média do(a) {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'

print(aluno)