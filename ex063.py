#Exercício Python #063 - Sequência de Fibonacci v1.0
total = 0
a = 0
b = 1
print('-' * 20, ' Gerador de sequência de fibonacci ', '-' * 20)
termos = int(input('Quantos termos você quer mostrar? '))
while total < termos:
    total += 1
    print( a, end=" -> " if total < termos else " -> Fim.")
    a = b - a
    b = b + a