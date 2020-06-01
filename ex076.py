#Exercício Python #076 - Lista de Preços com Tupla
lista = ('Lápis', 1.5, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.90)
print('-'*50)
print(f'{"Lista de preços":^50}')
print('-'*50)
for item in range(0, len(lista)):
    if item %2 == 0:
        print(f'{lista[item]:.<40}', end='')
    else:
        print(f'R$ {lista[item]:>6.2f}')
print('-'*50)