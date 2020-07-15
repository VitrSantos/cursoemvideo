#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior = menor = n1
if n1 > n2: menor = n2
if n1 > n3: menor = n3
if n1 < n2: maior = n2
if n1 < n3: maior = n3
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')

