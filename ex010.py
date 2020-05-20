d = float(input('Quanto de dinheiro você tem na carteira? R$: '))
print('Com',d ,'R$, você pode comprar \033[31mUS$ {:.2f}\033[m'.format(d / 5.07))