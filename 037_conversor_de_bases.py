'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 - para binário; 
2 - para octal; 
3 - para hexadecimal.'''

numero = int(input('Digite o número que deseja converter: '))

base = int(input('Qual será a base de conversão? \n'
                 f'[1] Binário \n'
                 f'[2] Octal \n'
                 f'[3] Hexadecimal'))

if base == 1:
    print(f'O número {numero} convertido para binário equivale à \n >>> '
          f'{bin(numero) [2:]}.')

elif base == 2:
    print(f'O número {numero} convertido para octal equivale à \n >>> '
          f'{oct(numero) [:2]}.')

elif base == 3:
    print(f'O número {numero} convertido para hexadecimal equivale à \n >>> '
          f'{hex(numero) [2:]}.')
