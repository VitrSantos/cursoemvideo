#Exercício Python #074 - Maior e menor valores em Tupla
from random import randint
numeros = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
print ('Os números sorteados foram:', end=' ')
for c in numeros:
    print(c, end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}.')
print(f'O menor valor sorteado foi {min(numeros)}.')