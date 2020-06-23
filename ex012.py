#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = (float(input('Qual o preço do produto? R$ ')))
print(f'Com 5% de desconto seu produto custará \033[032m{preço * 0.95}')