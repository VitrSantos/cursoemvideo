v = float(input('Qual a velocidade do carro (km/h)? '))
m = v - 80
vm = m * 7
if v > 80:
    print('MULTADO! você estava dirigindo acima do limite de velocidade que é de 80km/h')
    print('O valor a ser pago pela multa é de R${:.2f}'.format(vm))
print('Tenha um bom dia e dirija com segurança!')