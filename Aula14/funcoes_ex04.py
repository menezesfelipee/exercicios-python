# Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5nas horas extras trabalhadas.

def salario(valorHora, horas):
    if horas <= 40:
        return horas * valorHora
    else:
        return (40 * valorHora) + ((horas - 40) * valorHora * 1.5)

valorHora = float(input('Digite o valor que o empregado recebe por hora trabalhada em R$: '))
horas = float(input('Digite a quantidade de horas trabalhadas por esse funcionário: '))

print(f'Esse funcionário deverá receber R$ {salario(valorHora, horas):.2f} nesse mês.')
