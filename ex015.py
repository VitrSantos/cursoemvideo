#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram percorridos? '))
print('-='*20)
print(f'O valor a ser pago pelo aluguel do carro é de R${(dias*60)+(km*0.15):.2f}.')
print(f'R${dias*60} por aluguel de {dias} dias.\nE R${km*0.15:.2f} em função da quilometragem percorrida.')
