#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Salário atual: R$ '))
print(f'Com o reajuste salarial de 15%, um funcionario que ganhava {sal:.2f} passará a ganhar R$ {sal * 1.15:.2f}.')
