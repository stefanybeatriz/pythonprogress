'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

# Preparando as ferramentas core do jogo:
from random import choice
numeros = [1, 2, 3, 4, 5]
resposta = choice(numeros)

# Introdução
print('Será que você consegue advinhar em qual número o computador está pensando?')

# Palpite do usuário
palpite = int(input('Digite um número inteiro de 1 a 5: \n >> '))

print('Hmmm...')

# Conclusão
if palpite == resposta:
    print('Parabéns!! Você acertou!')
else:
    print('Ops! Não era este o número que o computador estava pensando.')

