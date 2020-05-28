nums = 'Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    escolha = int(input('Digite um número de 0 a 20: '))
    if 0 <= escolha <= 20:
        break
print(f'O número que você digitou escrito por extenso é {nums[escolha]}.')