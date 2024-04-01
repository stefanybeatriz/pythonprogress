# Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

from random import choice

nome1 = str(input('Digite o nome do aluno: '))
nome2 = str(input('Digite o nome do aluno: '))
nome3 = str(input('Digite o nome do aluno: '))
nome4 = str(input('Digite o nome do aluno: '))

alunos = [nome1, nome2, nome3, nome4]
escolhido = choice(alunos)

print(f'O aluno escolhido para apagar o quadro foi: \n >>> {escolhido}!')
