# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

numero = int(input('Digite um número inteiro: '))

divisoes = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        divisoes += 1

if divisoes == 2:
    print(f'O número {numero} é um número primo')
else:
    print(f'O número {numero} não é um número primo')

