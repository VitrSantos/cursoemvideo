#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

elemento = ('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(elemento)}')
print(f'Só tem espaços? {elemento.isspace()}')
print(f'É um número? {elemento.isnumeric()}')
print(f'É alfabético? {elemento.isalpha()}')
print(f'É alfanumérico? {elemento.isalnum()}')
print( f'Está em maiúsculo? {elemento.isupper()}')
print(f'Está em minúsculo? {elemento.islower()}')
print(f'Está capitalizada? {elemento.istitle()}')
