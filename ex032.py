from datetime import date
a = int(input('Que ano você quer analizar? '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é BISSEXTO'.format(a))
else:
    print('O ano {} informado não é BISSEXTO'.format(a))