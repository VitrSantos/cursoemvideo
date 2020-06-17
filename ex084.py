#Exercício Python #084 - Lista composta e análise de dados
resp = 's'
lista = []
galera = []
maiorp = menorp = cont = 0
pessoamen = pessoamai = ''
while resp in 'sS':
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    lista.append(nome)
    lista.append(peso)
    galera.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for p in galera:
    if cont == 0:
        maiorp = menorp = p[1]
    if p[1] >= maiorp:
        maiorp = p[1]
        pessoamai = p[0]
    if p[1] <= menorp:
        menorp = p[1]
        pessoamen = p[0]
    cont += 1
print(f'O maior peso foi de {pessoamai} que pesa {maiorp} ')
print(f'O menor peso foi de {pessoamen} que pesa {menorp}')