print('-=-' * 55)
print('Vou pensar em um número de 0 a 5, tente adivinhar!')
print('-=-' * 55)
from random import choice
from time import sleep
l = [0, 1, 2, 3, 4, 5,]
e = choice(l)
n1 = int(input('Qual número você chuta? '))
print('Processando...')
sleep(2)
if n1 == e:
    print('Parabéns, você acertou!.')
else:
    print('Ganhei, o número que eu pensei foi {}'.format(e))

