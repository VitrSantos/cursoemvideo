k = float(input('Quantos quilômetros terá sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}km'.format(k))
p = k * 0.50 if k <= 200 else k * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(p))



