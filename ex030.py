#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Me diga um número qualquer: '))
resto = num % 2
print('O número digitado é',end=' ')
if resto == 0:
    print('PAR')
else:
    print('ÍMPAR')


