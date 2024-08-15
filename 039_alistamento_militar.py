'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- se ele ainda vai se alistar ao serviço militar
- se é a hora exata de se alistar
- ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

# Calculo da idade
nascimento = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - nascimento

print(f'De acordo com o dado fornecido, você tem {idade} anos, logo:')

if idade < 18:
    print(f'Faltam {18 - idade} anos para você se alistar.')

elif idade == 18:
    print('Você deve se alistar imediatamente.')

elif idade > 18:
    print(f'Você deveria ter se alistado à {idade - 18} anos')

