#Exercício Python #080 - Lista ordenada sem repetições
lista = []
for c in range (0,5):
    n = int(input('Digite um número: '))
    if c  == 0 or n > lista[-1]:
        lista.append(n)
        print('Número adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Número adicionado na posição {pos}')
                break
            pos += 1
print(f'Os número digitados em ordem foram {lista}')