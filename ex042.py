x = float( input( 'Digite o cumprimento da primeira reta: ' ) )
y = float( input( 'Digite o cumprimento da segunda reta: ' ) )
z = float( input( 'Digite o cumprimento da terceira reta: ' ) )
if x < y + z and y < x + z and z < y + x:
    print(' Os segmentos podem formar um triângulo ', end='')
    if x == y == z:
        print('EQUILÁTERO')
    elif x == y or x == z:
        print('ISÓCELES')
    else:
        print('ESCALENO')
else:
    print( 'O triangulo não pode ser formado!' )
