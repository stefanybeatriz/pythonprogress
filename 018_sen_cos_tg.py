# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

angulo = int(input('Digite um ângulo qualquer: '))
radiano = radians(angulo)

print(f'Seno, cosseno e tangente do ângulo de {angulo} graus equivalem a: \n'
 f'Seno = {sin(radiano):.2f}; \n'
 f'Cosseno = {cos(radiano):.2f}; \n'
 f'Tangente = {tan(radiano):.2f}')
