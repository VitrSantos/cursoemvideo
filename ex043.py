print('\033[31m====================================\033[m Calculadora de IMC\033[31m ===========================================\033[m')
# massa dividido pelo quadrado da altura
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
calculo = peso / (altura * altura)
print('O seu IMC é {:.1f}.'.format(calculo))
if calculo < 18.5:
    print('Você está ABAIXO DO PESO ideal.')
elif 18.5 <= calculo < 25:
    print('Você está no PESO IDEAL.')
elif 25 <= calculo < 30:
    print('VOcê está em SOBREPESO.')
elif 30 <= calculo < 40:
    print('Você está com OBESIDADE')
elif calculo > 40:
    print('Você está com OBESIDADE MORBIDA, CUIDADO!')
