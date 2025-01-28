'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''

tentativas = 1

# Preparando a 'jogada' do computador:
from random import choice
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
resposta = choice(numeros)

# Introdução
print('Será que você consegue advinhar em qual número o computador está pensando?')

# Palpite do usuário
palpite = int(input('Digite um número inteiro de 1 a 10: \n >> '))

while palpite != resposta:
    palpite = int(input('Palpite errado, tente novamente: \n >> '))
    tentativas += 1

print(f'Parabéns, você acertou em {tentativas} tentativas!')
