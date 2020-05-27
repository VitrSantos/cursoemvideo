from math import trunc
qtd50 = qtd20 = qtd10 = qtd1 = 0
print('='*40)
print(' '* 13, 'BANCO CEV')
print('='*40)
valor = int(input('Quanto você quer sacar? R$ '))
resto = valor
while resto != 0:
    if valor > 50:
        qtd50 = valor / 50
        resto = valor % 50
        print(f'Você receberá {trunc( qtd50 )} notas de R$50.')
    if resto > 20:
        qtd20 = resto / 20
        resto = resto % 20
        print( f'Você receberá {trunc( qtd20 )} notas de R$20.' )
    if resto > 10:
        qtd10 = resto / 10
        resto = resto % 10
        print( f'Você receberá {trunc( qtd10 )} notas de R$10.' )
    if resto < 10:
        qtd1 = resto
        print(f'Você receberá {trunc( qtd1 )} notas de R$1.' )
        break
print('Volte sempre ao BANCO CEV. Tenha um bom dia!')