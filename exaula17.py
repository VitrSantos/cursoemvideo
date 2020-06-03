'''Listas
# As listas são estruturas similares às tuplas, mas são indicadas por colchetes[].
#Além disso, as listas apresentam a característica de serem mutáveis ao contrário das tuplas
Há comandos como:
lista.append(objeto) #(adiciona ao começo3 da lista)
lista.insert(posição,objeto) #(adiciona em posições ao longo da lista)
del lista[posição] #deleta itens em determinada posição
lista.pop(posição) #deleta itens, quando em branco, apaga o ultimo elemento
lista.remove(conteudo) #apaga os itens de acordo com o conteúdo, independente da posição
lista.sorted(reverse=True)'''
#Exemplos:
#num = [2,5,9,1]
#num[2] = 3
#num.append(7)
#num.sort(reverse=True)
#print(num)
#Exemplo 2:
valores  = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista')