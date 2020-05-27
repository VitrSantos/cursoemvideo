tot = tot1000 = cont = menor = barato = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = int(input('Preço: R$ '))
    tot += preço
    cont += 1
    if preço >= 1000:
        tot1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp =' '
    while resp not in 'SN':
        resp = str(input('Você quer adicionar mais produtos? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total da sua compra foi de R$ {tot:.2f}')
print(f'você comprou {tot1000} produtos que custaram mais de R$ 1000.00')
print(f'O produto mais barato comprado foi {barato} e seu preço é R${menor:.2f}')