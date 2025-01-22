# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

pesos = []

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    pesos.append(peso)

pesos_ordenados = sorted(pesos)

print(f'O menor peso lido foi: {pesos_ordenados[0]}kg \n'
      f'O maior peso lido foi: {pesos_ordenados[-1]}kg')

