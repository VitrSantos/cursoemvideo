#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
n1 = str(input('Nome do aluno: '))
n2 = str(input('Nome do aluno: '))
n3 = str(input('Nome do aluno: '))
n4 = str(input('Nome do aluno: '))
from random import shuffle
lista = [n1, n2, n3, n4]
ordem = shuffle(lista)
print(lista)
