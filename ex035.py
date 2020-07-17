#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print(20*"-=")
print('Analizador de triângulos')
print(20*"-=")
x = float(input('Digite o cumprimento da primeira reta: '))
y = float(input('Digite o cumprimento da segunda reta: '))
z = float(input('Digite o cumprimento da terceira reta: '))
if x < y + z and y < x + z and z < y + x:
    print('As retas podem formar um triângulo')
else:
    print('Não é possível formar um triângulo')
