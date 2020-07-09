#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Qual é seu nome? ')).upper()
pos = nome.find('SILVA')
fim = pos + 4
print(f'Seu nome tem Silva? {nome[pos:pos + 5] == "SILVA"}')
