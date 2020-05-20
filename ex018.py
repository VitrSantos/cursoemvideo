import math
a = int(input('digite um ângulo: '))
ar = math.radians(a)
print('O Seno do angulo de {} é igual a {:.2f}'.format(a, math.sin(ar)))
print('O Cosseno do ângulo de {} é de {:.2f}'.format(a, math.cos(ar)))
print('A tangente do ângulo de {} é de {:.2f}'.format(a, math.tan(ar)))
