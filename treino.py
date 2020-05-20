print('=' * 20, ' Gerador de PA ', '=' * 20)
primeiro = int(input('Qual é o termo incial? '))
raz = int(input('Razão da PA: '))
pa = primeiro
decimo = 0
mostrar = 1
mais = 10
print('Os dez primeiros termos dessa PA são:')
while mostrar != 0:
    while decimo < mais:
        print(' {} -> '.format(pa), end='' )
        decimo += 1
        pa += raz
    print('PAUSA')
    mostrar = int(input('Quantos termos você quer mostrar? '))
    mais = mais + mostrar
print('Progressão finlizada com {} termos mostrados'.format(mais))

