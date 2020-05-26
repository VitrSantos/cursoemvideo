'''
Para repetições infinitas, é usado o While True.
cont = 0
while True:
    cont += 1
    print(cont)'''
#Para parar repetições, é usado o comando break.
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.') #Uso das f strings para substituir o .format()