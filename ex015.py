d = int(input('O carro foi alugado por quantos dias? '))
k = float(input('Quantos quilômetros foram percorridos com esse carro? '))
vd = d * 60
vk = k * 0.15
print('O valor a ser pago pelo aluguel do carro é de R$ {:.2f}'.format(vk + vd))