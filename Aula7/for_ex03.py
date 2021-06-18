maiores = menores = 0
for c in range(7):
    ano = int(input('Digite seu ano de nascimento: '))
    if 2021 - ano >= 18:
        maiores += 1
    else:
        menores += 1
print(f'{maiores} pessoas são maiores de idade e {menores} ainda não são.')