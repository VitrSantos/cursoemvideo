nasc = int(input('Insira a data de nascimento do atleta: '))
from datetime import datetime
idd = datetime.today().year - nasc
print('O atleta tem {} anos.'.format(idd))
if idd <= 9:
    print('Classificação: \033[34mMIRIM')
elif idd <= 14:
    print('Classificação: \033[34mINFANTIL')
elif idd <= 19:
    print('Classificação: \033[34mJUNIOR ')
elif idd <= 25:
    print('Classificação: \033[34mSÊNIOR')
else: print('Classificação: \033[34mMASTER')
