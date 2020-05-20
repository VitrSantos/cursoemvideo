from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
pred = idade - 18
pred2 = 18 - idade
alistamento = date.today().year - pred
futuro = date.today().year + pred2
sexo = print('''Você é homem ou mulher? 
M = Mulher
H = Homem''')
opç = input('Opção ').upper()
print('Sua idade atual é de {} anos.'.format(idade))
if opç == 'H':
    if idade > 18:
        print('Você já deveria ter se alistado há {} ano(s)'.format(pred))
        print('Seu alistamento foi em {}'.format(alistamento))
    elif idade == 18:
        print('Seu alistamento deve acontecer IMEDIATAMENTE!')
    else:
        print('Seu alistamento ocorrerá em {}'.format(futuro))
if opç == 'M':
    print('O alistamento militar feminino não é obrigatório no Brasil e não tem data definida. Você pode se voluntariar procurando a junta de serviço militar mais próxima.')