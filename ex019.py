import random
n1 = input('digite um nome: ')
n2 = input('digite um nome: ')
n3 = input('digite um nome: ')
n4 = input('digite um nome: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))

