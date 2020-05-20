a = int(input('primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
#Verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor número digitado foi {}'. format(menor))
print('O maior número digitado foi {}'.format(maior))


