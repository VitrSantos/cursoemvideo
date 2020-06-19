#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um número para ver seu antecessor e sucessor: '))
print(f'Você digitou o número {num}.\nSeu sucessor é {(num)+1}.\nE seu antecessor é {(num)-1}.')