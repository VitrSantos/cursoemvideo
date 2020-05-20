x = float(input('Qual o valor do salário do funcionário? '))
if x >=1251:
    aumento = x * 1.10
else: aumento = x * 1.15
print('O valor do novo salário será R$ {:.2f}'.format(aumento))