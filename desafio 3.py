print('Vamos fazer a sequência de Fibonacci?')
stop = int(input('Qual o último número?'))
a = 0
b = 1
while (b < stop):
    print(b)
    b = b + a
    a = b - a