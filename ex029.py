#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velo = float(input('Qual a velocidade atual do carro (Km/h)? '))
print()
if velo > 80:
    print('Multado! Você excedeu o limite permitido que é de 80 Km/h.')
    print(f'O valor a ser pago pela infração é: R$ {(velo - 80)* 7:.2f}')
else:
    print('Você está dentro do limite.')
print('Dirija com segurança!')