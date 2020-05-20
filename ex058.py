from random import randint
tentativas = 0
print('Sou seu computador...')
print('Eu pensei em um número de 0 a 10, tente adivinhar!')
computador = randint(0, 10)
print(computador)
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        elif jogador > computador:
            print('Menos... Tente novamente!')
print("Acertou com {} tentativas. Parabéns!".format(tentativas))



