qtd9 = loc3 = pares = 0
numeros = int(input('Digite um algarismo: ')), int(input('Digite outro algarismo: ')), int(input('Digite mais um algarismo: ')), int(input('Digite o útimo algarismo: '))
print(f'Você digitou os valores: {numeros}')
for c in numeros:
    if c == 9:
        qtd9 += 1
    if c == 3:
        loc3 += numeros.index(3)+1
    if c % 2 == 0:
        pares += 1
print(pares)
print(loc3)
print(qtd9)