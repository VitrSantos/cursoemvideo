#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Digite o nome de uma cidade: ')).strip()
primeiro = cidade.upper()
print(primeiro[:6] == 'SANTO ')