f = str(input('Digite sua frase:')).upper().strip()
na = f.count('A')
print(na)
print('A primeria letra A apareceu a na posição {}'.format(f.find('A')+1))
print('A última letra A aparece na posição {}'.format(f.rfind('A')+1))


