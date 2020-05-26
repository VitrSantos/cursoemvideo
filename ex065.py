#Exercício Python #065 - Maior e Menor valores
quant = total =  maior = menor = 0
resp = "S"
while resp == "S":
    num = int(input('Digite um número: '))
    quant += 1
    total += num
    if quant == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    resp = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
print('Você digitou {} números e a média entre eles é {:.2f}.'.format(quant, total / quant))
print("O menor valor foi {} e o maior foi {}.".format(menor, maior))