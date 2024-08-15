# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

lista = []

for valor in range(1, 4):
    valores = int(input(f'Digite o {valor}º valor: \n >>> '))
    lista.append(valores)

lista_ordenada = sorted(lista)

print(f'Menor valor dado: {lista_ordenada[0]} \n'
      f'Maior valor dado: {lista_ordenada[2]}')

