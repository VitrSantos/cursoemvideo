#Exercício Python #068 - Jogo do Par ou Ímpar
from random import randint
print("=-"*20)
print('Vamos jogar Par ou Ímpar')
while True:
    print("=-"*20)
    computador = randint(0,10)
    numjogador = int(input("Digite um valor: "))
    jogador = str(input('Par ou ímpar? ')).upper().strip()[0]
    print(jogador)
    soma = computador + numjogador
    print(f'Você jogou {numjogador} e eu joguei {computador}, total de {soma}.')
    if jogador == 'P':
        if soma % 2 == 0:
            print('É par. Você ganhou! '
                  'Vamos jogar outra vez...')
        else:
            print('É ímpar. GAME OVER!')
            break
    if jogador == 'I' or jogador == 'Í':
        if soma % 2 != 0:
            print('É ímpar. Você ganhou! '
                  'Vamos jogar outra vez...')
        else:
            print('É par. GAME OVER!')
            break