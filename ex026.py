#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print(f"Há um total de {frase.count( 'A' )} 'A' nessa frase")
print(f'O primeiro A está na posição {frase.find("A")+1}')
print(f'O último A está na posição {frase.rfind("A")+1}')
