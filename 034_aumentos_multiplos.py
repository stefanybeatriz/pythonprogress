'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
- Para salários superiores a R$1250,00, calcule um aumento de 10%. 
- Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Digite seu salário atual: \n >>> R$'))

if salario > 1250:
    print(f'Você recebeu um aumento de 10% no seu salário, passando a receber agora: \n '
          f'>>> R${salario + (salario * 0.10)}')

elif salario <= 1250:
    print(f'Você recebeu um aumento de 15% no seu salário, passando a receber agora: \n '
          f'>>> R${salario + (salario * 0.15)}')

