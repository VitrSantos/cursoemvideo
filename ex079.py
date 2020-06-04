#Exercício Python #079 - Valores únicos em uma Lista
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso')
    else:
        print('Número duplicado, não vou adicionar')
    continuar = str(input('Você quer continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
print('-=' * 40)
print(sorted(lista))