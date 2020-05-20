s = float(input('Qual é salário do funcionário? '))
print('O salário do funcionário é de', s,'. Sendo assim, com \033[4;35m 15%\033[m de aumento, ele receberá \033[1;36m{:.2f}\033[m'.format(s * 1.15))