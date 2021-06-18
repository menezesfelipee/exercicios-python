num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('\nEscolha uma das opções: '))
    if opcao == 1:
        print(f'\nA soma {num1} + {num2} é igual a {num1 + num2}')
    if opcao == 2:
        print(f'\nA multiplicação {num1} x {num2} é igual a {num1 * num2}')
    if opcao == 3:
        if num1 > num2:
            print(f'\nO maior número é o {num1}')
        elif num1 < num2:
            print(f'\nO maior número é o {num2}')
        else:
            print('\nO números digitados são iguais.')
    if opcao == 4:
        num1 = float(input('\nDigite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))