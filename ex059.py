num = int(input('Digite um valor: '))
num2 = int(input(('Digite outro valor: ')))
sair = False
from time import sleep
while not sair:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opçao = int(input('>>>>>> Qual é a sua opção? '))
    if opçao == 5:
        sair = True
    elif opçao == 1:
        print('A soma de {} e {} é igual a {}'.format(num, num2, num + num2))
    elif opçao == 2:
        print('A multiplicação de {} e {} é igual a {}'.format(num, num2, num * num2))
    elif opçao == 3:
        maior = num
        if num2 > num:
            maior = num2
        print('O maior número entre {} e {} é {}'.format(num, num2, maior))
        if num == num2:
            print('Os dois valores são iguais')
    elif opçao == 4:
        nnum = int(input('Digite um novo valor: '))
        nnum2 = int(input('Digite um outro valor: '))
        num = nnum
        num2 = nnum2
    else:
        print('Opção inválida. Tente novamente!')
    sleep(2)
    print( "=" * 40 )
print('Obrigado por usar o programa. Até a próxima!')

