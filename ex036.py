casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
tempo = int(input('Em quantos anos a casa será paga? '))
t = tempo * 12
parcela = casa / t
condição = 0.3 * salario
if parcela <= condição:
    print('O valor da parcela será de R${:.2f} por mês em {} anos. Seu emprestimo será \033[4;32mCONCEDIDO'.format(parcela, tempo))
else:
    print('O valor da parcela será de R${:.2f} por mês em {} anos. Seu empréstimo será \033[4;31mNEGADO'.format(parcela, tempo))