soma = 0
cont = 0
for n in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} número(s) pares e a soma é {}'. format(cont, soma))