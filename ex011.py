#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
L = float(input('Qual a largura da parede? '))
H = float(input('Qual a altura da parede? '))
print(f'Sua parede tem as dimensões {L} X {H} e sua área é de {L*H:.2f} m²')
print(f'Para pintar essa parede, você precisará de {(L*H)/2:.2f} litros de tinta.')

