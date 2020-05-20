n = input('digite o nome de um aluno: ')
n1 = input('digite o nome de um aluno: ')
n2 = input('digite o nome de um aluno: ')
n3 = input('digite o nome de um aluno: ')
l = [n, n1, n2, n3]
import random
o = random.shuffle(l)
print('A ordem de apresentação dos trabalhos será {}'.format(l))