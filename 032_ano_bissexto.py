#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Digite um ano qualquer ou digite 0 para saber sobre o ano atual: '))

# Ano atual:
if ano == 0:
    ano = date.today().year

# Ano pré-definido:
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é bissesto!')
else:
    print(f'{ano} não é bissesto!')
