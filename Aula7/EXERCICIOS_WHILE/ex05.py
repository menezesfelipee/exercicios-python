total = cont1 = cont2 = cont3 = contNulos = contBrancos = 0
while True:
    print('''\nOs códigos para votar são:
    [ 1 ] José
    [ 2 ] João
    [ 3 ] Geraldo
    [ 4 ] Nulo
    [ 5 ] Branco
    [ 6 ] Finalizar votação''')
    voto = int(input('\nQual é o seu voto? '))
    if voto != 6:
        total += 1
    else:
        break
    if voto == 1:
        cont1 += 1
    if voto == 2:
        cont2 += 1
    if voto == 3:
        cont3 += 1
    if voto == 4:
        contNulos += 1
    if voto == 5:
        contBrancos += 1
print(f'''\nO total foi de {total} votos.
José recebeu {cont1} votos.
João recebeu {cont2} votos.
Geraldo recebeu {cont3} votos.
Tiveram {contNulos} votos nulos, o que equivale a {contNulos/total*100:.2f}% do total.
Tiveram {contBrancos} votos brancos, o que evivale a {contBrancos/total*100:.2f}% do total.''')