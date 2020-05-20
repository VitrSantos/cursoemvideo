print('=' * 25)
print(' Os 10 termos de uma PA')
print('=' * 25)
inc = int(input('Qual é o primeiro termo? '))
rz = int(input('Qual é a razão? '))
dec = inc + (10 - 1) * rz
for c in range(inc, dec + rz, rz):
    print(c, end=" -> ")
