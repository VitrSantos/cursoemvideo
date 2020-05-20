print('========================= Lojas Santos ===========================')
price = float(input('Valor total: R$ '))
print('''FORMA DE PAGAMENTO:
[1] à vista dinheiro/cheque 
[2] à vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opçao = int(input('Opção: '))
if opçao == 1:
    print('Sua compra será paga á vista com dinheiro ou cheque.')
    print('Sua compra de R${} vai custar R${:.2f}.'.format(price, price * 0.9))
elif opçao == 2:
    print('Sua compra será paga à vista no cartão.')
    print('Sua compra de R${} vai custar R${:.2f}.'. format(price, price * 0.95))
elif opçao == 3:
    print('Sua compra será paga em 2 vezes no cartão.')
    print('O valor de sua compra não sofrerá alteração.')
elif opçao == 4:
    parcelas = int(input('Em quantas vezes você deseja pagar? (máx 12x) '))
    if 3 <= parcelas <= 12:
        print('Sua compra será paga em {}x no cartão COM JUROS'.format(parcelas))
        print('Sua compra de valor R${} passará a custar R${:.2f}.'.format(price, price * 1.2))
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')