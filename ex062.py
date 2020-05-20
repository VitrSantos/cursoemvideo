primeiro = int(input('Termo inicial: '))
razao = int(input(('Razão: ')))
decimo = 1
pa = primeiro
total = 0
mais = 10
print('Os dez primeiros termos dessa PA são:', end=' ')
while mais != 0:
    total = total + mais
    while decimo <= total:
        print(' {} ->'.format(pa), end='')
        decimo += 1
        pa += razao
    print(' PAUSA')
    mais = int(input(' Quantos termos você quer mostrar a mais? '))
print('progressão finalizada com {} termos mostrados'.format(total))
