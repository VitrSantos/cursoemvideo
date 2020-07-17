#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = int(input('Qual é o valor da casa? '))
salario = float(input("Quanto você ganha? "))
tempo = int(input('Quantos anos de financiamento? '))
prestaçoes = casa / (tempo * 12)
print('-'*40)
print(f'Para financiar uma casa de R$ {casa} por {tempo} anos, a parcela será de {prestaçoes:.2f}')
if prestaçoes <= salario * 0.3:
    print('O empréstimo será CONCEDIDO!')
else:
    print('O empréstimo será NEGADO!')

