'''Faça um programa que leia uma frase pelo teclado e mostre: 
- Quantas vezes aparece a letra "A"; 
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).lower().strip()

# Quantas vezes aparece a letra "A":
total_a = frase.count('a')
print(f'A letra A aparece {total_a} vezes nessa frase')

# Posição em que a letra "A" aparece pela primeira vez:
primeira = frase.find('a') + 1
print(f'A letra A aparece pela primeira vez na posição {primeira} da frase')

# Posição em que a letra "A" aparece pela última vez:
ultima = frase.rfind('a') + 1
print(f'A letra A aparece pela última vez na posição {ultima} da frase')

