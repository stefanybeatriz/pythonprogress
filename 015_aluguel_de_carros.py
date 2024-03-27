'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
Calcule o preço a pagar, sabendo que:
- o carro custa R$60 por dia 
- R$0,15 por Km rodado'''

distancia = float(input('Quantos kilômetros o carro percorreu? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

total_distancia = distancia * 0.15
total_dias = dias * 60
total_a_pagar = total_distancia + total_dias

print(f'O valor total a ser pago equivale a R${total_a_pagar}')
