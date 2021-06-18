# Modo 1
l = [5, 7, 2, 9, 4, 1, 3]
print(f'''Tamanho: {len(l)}
Maior valor: {max(l)}
Menor valor: {min(l)}
Soma de todos os itens: {sum(l)}
Lista em ordem crescente: {sorted(l)}
Lista em ordem decrescente: {sorted(l, reverse=True)}''')


# Modo 2
l = [5, 7, 2, 9, 4, 1, 3]
print(f'''Tamanho: {len(l)}
Maior valor: {max(l)}
Menor valor: {min(l)}
Soma de todos os itens: {sum(l)}''')
l.sort()
print(f'Lista em ordem crescente: {l}')
l.reverse()
print(f'Lista em ordem decrescente: {l}')