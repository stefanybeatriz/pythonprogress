# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: \n')) .replace(' ', '') .lower()

frase_invertida = frase[::-1]

if frase == frase_invertida:
    print('Esta frase é um palíndromo')
else:
    print('Esta frase não é um palíndromo')

