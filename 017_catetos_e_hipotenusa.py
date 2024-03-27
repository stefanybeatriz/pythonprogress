# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa

from math import sqrt

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

catetos = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = sqrt(catetos)

print(f'O comprimento da hipotenusa equivale a {hipotenusa}cm')
