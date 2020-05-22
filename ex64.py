#Exercício Python #064 - Tratando vários valores v1.0
cont = soma = 0
Flag = False
while not Flag:
    num = int( input( 'Digite um número [999 para parar]: ' ) )
    if num == 999:
            Flag = True
    else:
        cont += 1
        soma += num
print('Você digitou {} algarismos e a soma deles é {}.'.format(cont, soma))
