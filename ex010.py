#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dinheiro = float(input("Quanto dinheiro você tem no momento (reais)? "))
print(f'Com R${dinheiro:.2f} você pode comprar {dinheiro/3.27:.2f} Dólares.')