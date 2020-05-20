maior = 0
menor = 0
for c in range(1, 6):
    peso = float( input( f'Qual o peso da {c}ª pessoa? ' ) )
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('''O maior peso lido foi de {:.2f}.
E o menor peso lido foi de {:.2f}.'''.format(maior, menor))
