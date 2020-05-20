primeiro = int(input('Termo inicial: '))
razao = int(input(('Razão: ')))
decimo = 1
pa = primeiro
print('Os dez primeiros termos dessa PA são:', end=' ')
while decimo <= 10:
    print(pa, end=' -> ' if decimo < 10 else '.')
    decimo += 1
    pa += razao

