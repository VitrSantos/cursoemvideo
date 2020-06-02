palavras = ('curso', 'video', 'python', 'aprender', 'programar', 'linguagem', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nA palavra {p.upper()} tem as vogais: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')