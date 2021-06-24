# Sexo Biológico

sexo = input('Digite seu sexo: [M/F]').strip().upper()[0]
while True:
    if sexo not in 'MF':
        sexo = input('Digite seu sexo novamente: [M/F]').strip().upper()[0]
    else:
        break
if sexo == 'M':
    print('Seu sexo é masculino')
else:
    print('Seu sexo é feminino')