'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = str(input('Informe seu sexo (M ou F): ')).strip() .upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dado inválido. Tente novamente: ')).strip() .upper()[0]

print(f'Sexo: {sexo}\nValidação completa')
