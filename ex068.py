#Exercício Python #068 - Jogo do Par ou Ímpar
from random import randint
cont = 0
print("=-"*20)
print('Vamos jogar Par ou Ímpar')
while True:
    print("=-"*20)
    computador = randint(0,10)
    numjogador = int(input("Digite um valor: "))
    jogador = str(input('Par ou ímpar? ')).upper().strip()[0]
    soma = computador + numjogador
    print(f'Você jogou {numjogador} e eu joguei {computador}, total de {soma}.')
    if jogador == 'P':
        if soma % 2 == 0:
            print('É par. Você ganhou! '
                  'Vamos jogar outra vez...')
            cont += 1
        else:
            print(f'É ímpar. GAME OVER! você ganhou {cont} vez(es).')
            break
    elif jogador == 'I' or jogador == 'Í':
        if soma % 2 != 0:
            print('É ímpar. Você ganhou! '
                  'Vamos jogar outra vez...')
            cont += 1
        else:
            print(f'É par. GAME OVER! você ganhou {cont} vez(es).')
            break