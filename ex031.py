#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distância = float(input('Qual é a distância(Km) da sua viagem? '))
tarifa = 0
if distância <= 200:
    tarifa = 0.5
else:
    tarifa = 0.45
print(f'Você está prestes a fazer uma viagem de {distância}\n'
      f'E o valor da sua passagem será de R$ {(distância * tarifa):.2f}')
