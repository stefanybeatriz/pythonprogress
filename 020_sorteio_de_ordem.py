# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

nome1 = str(input('Digite o nome do aluno: '))
nome2 = str(input('Digite o nome do aluno: '))
nome3 = str(input('Digite o nome do aluno: '))
nome4 = str(input('Digite o nome do aluno: '))

alunos = [nome1, nome2, nome3, nome4]
shuffle(alunos)

print(f'A ordem dos alunos a apresentar será {alunos}')
