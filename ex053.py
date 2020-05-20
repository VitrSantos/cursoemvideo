frase = str(input('Insira uma frase: ')).upper().strip()
separado = frase.split()
junto = ''.join(separado)
inverso =''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(frase, inverso))
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')