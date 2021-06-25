'''Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

Nota   Conceito
>=9.0  A
>=8.0  B
>=7.0  C
>=6.0  D
>=5.0  E
<=4.0  F         '''

def conceito(nota):
    if nota >= 9:
        return 'A'
    elif nota >= 8:
        return 'B'
    elif nota >= 7:
        return 'C'
    elif nota >= 6:
        return 'D'
    elif nota >= 5:
        return 'E'
    else:
        return 'F'

nota = float(input('Digite a nota do aluno: '))

print(f'O conceito do aluno nessa prova foi {conceito(nota)}')
