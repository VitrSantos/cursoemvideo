'''from math import factorial
fatorial = int(input('Qual número você quer o fatorial? '))
print('O fatorial de {} é {}'.format(fatorial, factorial(fatorial)))'''

'''n = int(input('Qual número você quer o fatorial? '))
c = n
f = 1
print('Calculando o fatorial de {}!...'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

'''n = int(input("Qual número você quer descobrir o fatorial? "))
f = 1
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='',)
    f *= c
    print('{}'.format(f))'''

n = int( input( 'Digite um numero para calcular seu fatorial: ' ) )
c = 0
f = 1
for c in range( 1, n ):
    f *= n
    n -= 1
print( 'Seu fatorial é {}.'.format( f ) )
print(n)
