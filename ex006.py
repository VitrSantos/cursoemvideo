#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Digite um número: '))
print(f'O dobro desse número é {(num)*2}.\nO triplo desse número é {(num)*3}.\nA raiz quadrada desse número é {(num ** (1/2)):.2f}.')