n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2) / 2
print('O aluno que tem as notas {} e {} tem a média = {:.1f}'.format(n1, n2, media))
if media < 5:
    print('A situação do aluno é \033[31mREPROVADO.')
elif media <= 6.9:
    print('A situação do aluno é \033[33mRECUPERAÇÃO.')
elif media >= 7:
    print('a situação do aluno é \033[32mAPROVADO.')