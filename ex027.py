n = str(input('Digite seu nome completo: ')).upper().strip()
l = n.split()
print('Muito prazer em te conhecer {} {}'.format(l[0], l[len(l)-1]))