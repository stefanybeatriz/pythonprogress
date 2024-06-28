'''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: \n >> '))

# Nome com todas as letras maiúsculas: função upper
print(f'Em maiúsculo: {nome.upper()}')

# Nome com todas as letras minúsculas: função lower
print(f'Em minúsculo: {nome.lower()}')

# Quantidade de letras
# a) remoção dos espaços: função replace
nome_sem_espaco = (nome.replace(' ', ''))

# b) quantidade de letras sem os espaços
print(f'O nome {nome} tem {len(nome_sem_espaco)} caracteres')

# Quantidade de letras do primeiro nome
# a) separando as palavras da frase (nome): função split
parte_do_nome = nome.split()

# b) apresentando a quantidade de letras do primeiro nome: função len
print(f'O seu primeiro nome tem {len(parte_do_nome[0])} letras')

