# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.

maiores = menores = 0
lista = []
for i in range(5):
    nome = input(f'Digite o {i+1}º nome: ').capitalize()
    idade = int(input(f'Digite a idade do(a) {nome}: '))
    lista.append([nome, idade])
    print()
for i in lista:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade')
        maiores += 1
    else:
        print(f'{i[0]} é menor de idade')
        menores += 1
print(f'\n{maiores} pessoas são maiores de idade.\n{menores} pessoas são menores de idade.')
