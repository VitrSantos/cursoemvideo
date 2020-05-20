l = float(input('Quantos metros de largura tem a parede? '))
a = float( input('Quantos metros de altura tem a parede? '))
m2 = l * a
print('A sua parede tem as dimensões de', l, 'x', a, ' e a área total de', m2, 'm2')
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(m2 / 2))
