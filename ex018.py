#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ang = int(input('Digite o valor do ângulo: '))
ran = radians(ang)
print(f'O Seno do angulo é {sin(ran):.2f}.')
print(f'O Cosseno do angulo é {cos(ran):.2f}')
print(f'A tangente do ângulo é {tan(ran):.2f}')

