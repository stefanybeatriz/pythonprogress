# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

numero = int(input('Digite um número de 0 à 9999: \n >> '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Analisando este número, ele possui: \n'
    f'Unidades: {unidade} \n'
    f'Dezenas: {dezena} \n'
    f'Centenas: {centena} \n'
    f'Milhares: {milhar}')

