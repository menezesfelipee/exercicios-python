# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    return custo * (1 + taxaImposto)

tax = float(input('Digite a taxa de imposto em %: ')) / 100
valor = float(input('Digite o valor do item: '))

print(f'O valor do item após ser aplicado o imposto é de: R$ {somaImposto(tax, valor):.2f}')
