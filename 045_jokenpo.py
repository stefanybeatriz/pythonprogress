# Crie um programa que faça o computador jogar Jokenpô com você.

# Bibliotecas que utilizei
from random import choice
from time import sleep

print('Pedra, Papel e Tesoura!')

# Jogada do player
jogador = int(input('Faça sua escolha:\n'
                    '[1] Pedra\n'
                    '[2] Papel\n'
                    '[3] Tesoura\n'
                    '>>> '))

pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'

# Jogada do computador
escolhas = [pedra, papel, tesoura]
pc = choice(escolhas)

print('Hum...')
sleep(3)

# Condição de vitória do jogador
if jogador == 1 and pc == tesoura or jogador == 2 and pc == pedra or jogador == 3 and pc == papel:
    print(f'A máquina escolheu {pc}, você venceu! Parabéns!')

# Condição de derrota do jogador
elif jogador == 1 and pc == papel or jogador == 2 and pc == tesoura or jogador == 3 and pc == pedra:
    print(f'A máquina escolheu {pc}, você perdeu! \nMais sorte na próxima!')

# Empate
else:
    print(f'A máquina escolheu {pc}, parece que tivemos um empate! \nJogue novamente para desempatar!')

print('Obrigada por jogar!')

