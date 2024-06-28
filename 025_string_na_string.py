# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite seu nome completo: \n >> ')).upper()

if 'SILVA' in nome:
    print('Você possui o sobrenome Silva')
else:
    print('Você não possui o sobrenome Silva')

