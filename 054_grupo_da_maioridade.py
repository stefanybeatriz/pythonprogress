# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

# Obtendo o ano atual
from datetime import datetime
ano_atual = datetime.now().year

count_menores = 0
count_maiores = 0

for c in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if ano_atual - nascimento < 18:
        count_menores += 1
    else:
        count_maiores += 1

print(f'{count_menores} pessoas são menores de idade \n'
      f'{count_maiores} pessoas são maiores de idade')

