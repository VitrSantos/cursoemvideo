num = int(input('Qual número você deseja saber se é primo?  '))
tot = 0
for c in range(1, num + 1):
    if num % c ==0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vez(es).'.format(num, tot))
if tot <= 2:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} não é primo.'.format(num))