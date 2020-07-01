#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
n1= str(input('Nome do aluno: '))
n2 = str(input('Nome de outro aluno: '))
n3 = str(input('Nome de mais um aluno: '))
n4 = str(input('Nome do último aluno: '))
escolha = [n1, n2, n3, n4]
escolhido = choice(escolha)
print(escolhido)