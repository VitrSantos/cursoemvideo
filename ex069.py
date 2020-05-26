idade = homens = mulheres = 0
mais = "S"
while mais in "S":
    print('-=' * 20)
    print("Cadastre uma pessoa")
    print('-='*20)
    idd = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo == "M":
        homens += 1
    elif sexo == "F" and idade < 20:
        mulheres += 1
    if idd >= 18:
        idade += 1
    mais = str(input('Quer cadastrar mais alguém? [S/N] ')).upper().strip()[0]
    while mais not in "SN":
        mais = str( input( 'Quer cadastrar mais alguém? [S/N] ' ) ).upper().strip()[0]
while mais in 'N':
    print(f'''Total de pessoa com mais de 18 anos: {idade}\nTotal de homens cadastrados: {homens}\nTotal de mulheres com menos de 18 anos: {mulheres}''')
    break

