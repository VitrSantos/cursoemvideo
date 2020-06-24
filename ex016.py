#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input('Digite um número real: '))
print(f'Você digitou o número {num}. A parte interia do número digitado é: {num.__trunc__()}.')