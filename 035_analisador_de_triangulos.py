# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Digite o comprimento das 3 retas: ')

a = float(input('Reta A: '))
b = float(input('Reta B: '))
c = float(input('Reta C: '))

if a < b + c and b < a + c and c < b + c:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo.')

