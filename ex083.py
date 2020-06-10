#Exercício Python #083 - Validando expressões matemáticas
lista = str(input('Digite a sua expressão: '))
pilha = []
for c in lista:
    if c == '(':
        pilha.append(')')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
        break
print('=-'*30)
if len(pilha) > 0:
    print('A expresão não é válida')
elif len(pilha) == 0:
    print('A expressão é válida')