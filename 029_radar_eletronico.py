'''Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''

# Simulando a velocidade do veículo
velocidades = []
for km in range (1, 201):
    velocidades.append(km)

from random import choice
velocidade = choice(velocidades)

'''Explicação:
1) Criamos um range que vai de 1 a 200km/h
2) Colocamos esses valores dentro da lista velocidades
3) Usamos a biblioteca random para selecionar uma dessas kilometragens

Essa kilometragem aleatória será a base para sabermos se o veículo será multado ou não'''

# Cáluclo da multa:
multa = (velocidade - 20) * 7

# Simulação de funcionamento do radar
print(f'O veículo que ultrapassou o radar estava a: {velocidade}km/hora, logo:')

if velocidade <= 80:
    print('Este veículo está dentro dos limites de velocidade, logo não será multado.')
else:
    print(f'Este veículo ultrapassou os limites de velocidade e será multado em R${multa} reais')

