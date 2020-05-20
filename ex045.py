from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint (0, 2)
jogador = int(input('''Sua jogada
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO')
sleep(0.8)
print('-=' * 15 )
print('O computador escolheu {}'.format(itens[computador]))
print ('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 15 )
if computador == 0: # jogou pedra
    if jogador == 0:
        print('\033[33mEMPATE')
    if jogador == 1:
        print('\033[32mO jogador ganhou')
    if jogador == 2:
        print('\033[31mO computador venceu')
elif computador == 1: # jogou papel
    if jogador == 0:
        print('\033[31mO computador venceu')
    if jogador == 1:
        print(('\033[33mEMPATE'))
    if jogador == 2:
        print('\033[32mO jogador venceu')
elif computador == 2: # jogou tesoura
    if jogador == 0:
        print('\033[32mO Jogador venceu')
    if jogador == 1:
        print('\033[31mO computador venceu')
    if jogador == 2:
        print('\033[33mEMPATE')
