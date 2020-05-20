num = int(input('Qual número deseja converter? '))
print('''Digite [] para selecionar a base
[1] para binário
[2] para octal
[3] para haxadecimal''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('Seu número {} convertido em binário é igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('Seu número {} convertido em octal é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('Seu número {} convertido em hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else: print('Opção inválida. Tente novamente!')
