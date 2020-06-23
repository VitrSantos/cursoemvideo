#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Digite um valor em metros: '))
print(f'Os {metros} metros digitados correspondem a:')
print(f'Em quilômetros {metros * 0.001} Km')
print(f'Em Hectômetros {metros * 0.01} hm')
print(f'Em decâmetros {metros * 0.1} dam')
print(f'Em decímetros {metros * 10} dm')
print(f'Em centímetros {metros * 100} cm')
print(f'Em milímetros {metros * 1000} mm')
