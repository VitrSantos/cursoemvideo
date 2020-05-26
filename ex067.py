#Exercício Python #067 - Tabuada v3.0
while True:
    num = int(input('Qual número você quer ver a tabuada? (Digite números negativos para sair) '))
    if num < 0:
        print('Obrigado por usar a tabuada!')
        break
    for c in range(0, 11):
        print(f'{num} X {c} = {num * c}')
    print('-' * 40)
