#Exercício Python #075 - Análise de dados em uma Tupla
qtd9 = loc3 = pares = 0
numeros = int(input('Digite um algarismo: ')), int(input('Digite outro algarismo: ')), int(input('Digite mais um algarismo: ')), int(input('Digite o útimo algarismo: '))
print('=-'*20)
print(f'Os valores digitados foram {numeros}')
print((f'O algarismo 9 apareceu {numeros.count(9)} vezes'))
if 3 in numeros:
    print(f'O algarismo 3 apareceu na {numeros.index(3)}ª posição')
else:
    print('O algarismo 3 não foi digitado em nenhuma posição')
print( f'Os valores pares digitados foram', end=' ' )
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')