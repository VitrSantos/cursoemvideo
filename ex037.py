#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
base = int(input('Para qual base você deseja convertê-lo?\n[1] Binária\n[2] Octal\n[3] Hexadecimal\nOpção: '))
if base == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.')
elif base == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}.')
elif base == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')
else:
    print('Opção inválida, tente novamente!')