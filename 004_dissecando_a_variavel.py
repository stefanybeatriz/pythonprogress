# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele

a = input('Digite algo: ')

tipo = type(a)
print(f'O tipo primitivo dessa variável é {tipo}')

# Informações:
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está um minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

'''Exemplos com outras formas de resolver
1) print('O tipo primitivo desse valor é ', type(a))
2) print('O tipo primitivo desse valor é {}' .format(tipo))
3) print('O tipo primitivo desse valor é', tipo)'''
