lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]
print('-='*30)
print(f'Os numeros digitados foram {lista}')
print(f'O maior valor digitado foi {maior} que apareceu nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {menor} que apareceu nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')

