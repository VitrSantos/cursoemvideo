#Exercício Python #084 - Lista composta e análise de dados
pessoa = []
lista = []
maiorpeso = menorpeso = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    for p in lista:
        if len( lista ) == 1:
            menorpeso = maiorpeso = p[1]
    lista.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for p in lista:
    if maiorpeso < p[1]:
        maiorpeso = p[1]
    if menorpeso > p[1]:
        menorpeso = p[1]
print(f'O maior peso foi {maiorpeso}. Peso de', end=' ')
for p in lista:
    if p[1] == maiorpeso:
        print([p[0]], end=' ')
print()
print(f'O menor peso foi {menorpeso}. Peso de', end=' ')
for p in lista:
    if p[1] == menorpeso:
        print([p[0]], end=' ')