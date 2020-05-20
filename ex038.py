pr = int(input('Qual é o primeiro número? '))
se = int(input('Qual é o segundo número? '))
rs = pr - se
if rs == 0:
    print('Os dois número são iguais.')
elif rs < 0:
    print('O segundo número é maior.')
else: print('O primeiro número é maior.')