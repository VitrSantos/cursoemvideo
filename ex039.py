#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
nascimento = int(input('Em qual ano você nasceu? '))
sexo = int(input('Qual é o seu sexo\n[1] Feminino\n[2] Masculino\nOpção: '))
ano = datetime.datetime.today().year
if sexo == 2:
    if ano - nascimento == 18:
        print('Você tem que se alistar IMEDIATAMENTE.')
    elif ano - nascimento < 18:
        falta = ((ano - nascimento) - 18)
        print(f'Ainda não está na hora de se alistar. Seu alistamento irá ocorrer daqui a {-falta} ano(s), em {ano - falta}.')
    else:
        passou = ((ano - nascimento) - 18)
        print(f'O momento de seu alistamento já passou. Você deveria ter se alistado há {passou} ano(s), em {ano - passou}.\nDirija-se a uma junta de serviço militar o mais rápido possível!')
if sexo == 1:
    if ano - nascimento >= 18:
        print('O alistamento militar não é obrigatório para mulheres no Brasil.\nMas você já tem idade para se voluntariar.')
    else:
        falta = ((ano - nascimento) - 18)
        print(f'Ainda não está na hora de se alistar. Seu alistamento pode ocorrer daqui a {-falta} ano(s), em {ano - falta}.' )

