#Exercício Python #082 - Dividindo valores em várias listas
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        print(f'Os números digitados forma {lista}')
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os números pares digitados foram {pares}')
print(f'Os números impares digitados foram {impares}')