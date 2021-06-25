# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

def imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input('Digite seu peso em kg: '))
altura = int(input('Digite seu altura em cm: ')) / 100

print(f'Seu IMC é: {imc(peso, altura):.2f}')
