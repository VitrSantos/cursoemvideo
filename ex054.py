from datetime import date
cont = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        cont += 1
    else:
        cont2 += 1
print( 'existem {} pessoas maiores de idade.'.format( cont ) )
print('existem {} pessoas menores de idade.'.format(cont2))


