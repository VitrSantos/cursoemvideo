co = float(input('Digite o cateto oposto do triângulo retângulo: '))
ca = float(input('Digite o cateto adjacente do trângulo retângulo: '))
from math import sqrt
from math import pow
s = pow(co, 2) + pow(ca, 2)
print('A hipotenusa dos catetos acima é igual a {:.3f}'.format(sqrt(s)))

