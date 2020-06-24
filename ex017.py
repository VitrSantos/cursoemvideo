#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o cateto oposto do triângulo retângulo: '))
ca = float(input('Digite o cateto adjacente do trângulo retângulo: '))
print(f'A hipotenusa dos catetos acima é {math.hypot(co,ca) :.0f}')

