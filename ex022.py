#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome = str(input('Qual é o seu nome? '))
nomesemespaço = nome.strip()
nomes = nome.split()
print('Analisando o seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print( f'Seu nome em minúsculas é {nome.lower()}')
print(len(nome) - (nome.count(' ')))
print(len(nomes[0]))
