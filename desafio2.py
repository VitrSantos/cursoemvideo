Turno = input('Qual turno você estuda (M=Matutino, V=Vespertino, N= noturno)? ').upper()
nome = input('Qual seu nome? ')
if Turno == 'M':
    print('Bom dia,',nome ,'!')
elif Turno == 'V':
    print('Boa tarde,',nome ,'!')
else:
    print( 'Boa noite,',nome ,'!')