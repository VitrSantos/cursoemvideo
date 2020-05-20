x = float(input('Digite o cumprimento da primeira reta: '))
y = float(input('Digite o cumprimento da segunda reta: '))
z = float(input('Digite o cumprimento da terceira reta: '))
if x < y + z or y < x + z or z < y + x:
    print('O triângulo pode ser formado!')
else:
    print('O triangulo não pode ser formado!')
