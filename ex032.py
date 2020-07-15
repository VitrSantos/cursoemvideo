#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
atual = datetime.date.today().year
ano = int(input('Digite um ano para verificar se ele é bissexto: '))
if ano == 0:
    ano = atual
if ano % 4 == 0 or ano % 400 == 0:
    print(f"O ano de {ano} é bissexto!")
else:
    print(f'O ano de {ano} não é bissexto.')