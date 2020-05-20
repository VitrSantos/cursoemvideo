n = int(input('Qual número você quer a tabuada? '))
for c in range(0, 11):
    print('{} X {:2} = {}'.format(n, c, n * c))
