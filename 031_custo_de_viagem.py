# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Qual será a distância percorrida pelo veículo, em Km? \n >>> '))

if km <= 200:
    print(f'O preço da sua passagem será: {km * 0.50} reais.')
else:
    print(f'O preço da sua passagem será: {km * 0.45} reais.')
