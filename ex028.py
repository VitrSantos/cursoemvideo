#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import choice
num = 0, 1, 2, 3, 4, 5
computador = choice(num)
print('=-'*27)
print('Vou pensar em um número entre  0 e 5, tente adivinhar!')
print('=-'*27)
jogador = int(input('Qual o seu palpite? '))
print(f'O número em que pensei foi {computador}')
if jogador == computador:
    print('Você ganhou, parabéns!!!')
else:
    print('Você perdeu, tente novamente!')