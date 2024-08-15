'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
- Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
- A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('Sistema Automático de Aprovação de Empréstimos')

# Infos core
casa = float(input('Valor da casa: '))
salario = float(input('Seu salário: '))
anos = int(input('Em quantos anos deseja pagar: ')) * 12 # Conversão para meses

prestacao = casa // anos
limitador = salario * 0.30

print('De acordo com a quantidade de anos oferecidos: \n'
      f'- A prestação mensal será de: R${prestacao}')

if prestacao < limitador:
    print('EMPRÉSTIMO APROVADO \n'
          f'Valor mensal a ser pago: R${prestacao} durante {anos} meses')

else:
    print('EMPRÉSTIMO NEGADO \n'
          'O valor da prestação é superior a 30% da sua renda mensal')

