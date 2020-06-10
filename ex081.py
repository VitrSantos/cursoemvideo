#Exercício Python #081 - Extraindo dados de uma Lista
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = (str(input('Você quer continuar? [S/N] '))).upper().strip()
    if resp in 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')
