'''PARA INSERIR UMA COR DO PADRÃO ANSI NO PYTHON DIGITE: \033[STYLE;TEXT;BACKm'''
print('\033[31mTeste do exercício 34 com cores\033[m')
x = float(input('Qual o valor do salário do funcionário? '))
if x >=1251:
    aumento = x * 1.10
else: aumento = x * 1.15
print('O valor do novo salário será \033[32mR$ {:.2f}\033[m'.format(aumento))
