''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: 
 a média de idade do grupo, 
 qual é o nome do homem mais velho e 
 quantas mulheres têm menos de 20 anos. '''

# Variáveis que vão ser preenchidas
idades = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

# Loop para obtenção de dados
for c in range(1, 5):
    print(f'--- Dados da {c}ª pessoa: --- \n')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo (M ou F): ')) .upper()
    print('- - - - - - - - - -\n')

    # Soma das idades
    idades += idade

    # Determinando a idade do homem mais velho
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade 
        nome_homem_mais_velho = nome

    # Determinando a quantidade de mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

# Resultados:
print(f'A média de idade do grupo é: {idades / c} anos;\n'
      f'O nome do homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos;\n'
      f'{mulheres_menos_20} mulheres tem menos de 20 anos')
