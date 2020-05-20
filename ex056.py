somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('----- {}ª pessoa -----'.format(c))
    nome = str(input('Nome: '))
    idd = int(input('Idade: '))
    sex = str(input('Sexo [M\F]: ')).upper().strip()
    if c == 1 and sex in "Mm":
        maioridadehomem = idd
        nomevelho = nome
    if sex in 'mn' and idd > maioridadehomem:
        maioridadehomem = idd
        nomevelho = nome
    if sex in 'Ff' and  idd < 20:
        totmulher20 += 1
    somaidade += idd
mediaidade = somaidade / 4
print('A média de idade do grupo é {:.0f} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres de com menos de  20 anos'.format(totmulher20))


