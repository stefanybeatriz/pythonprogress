'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

# Adquirindo um valor aleatório de compra
preco_normal = []

for preco in range(1, 1001):
    preco_normal.append(preco)

from random import choice
preco_normal = choice(preco_normal)

# Qual meio de pagamento o cliente deseja utilizar
print(f'O valor total de sua compra foi de R${preco_normal} \n'
      'Selecione a condição de pagamento \n')

pagamento = int(input('Formas de pagamento disponíveis: \n'
                      '[1] À vista no dinheiro/cheque\n'
                      '[2] À vista no cartão\n'
                      '[3] Até 2x no cartão\n'
                      '[4] 3x ou mais no cartão\n'
                      '>>> '))

if pagamento == 1: # À vista no dinheiro/cheque
    print('\nVocê recebeu um desconto de 10% no valor da compra\n'
          f'Total a ser pago: R${preco_normal - (preco_normal * 0.1)}')

elif pagamento == 2: # À vista no cartão
    print('\nVocê recebeu um desconto de 5% no valor da compra\n'
          f'Total a ser pago: R${preco_normal - (preco_normal * 0.05)}')

elif pagamento == 3: # 2x no cartão
    print(f'Você optou por dois pagamentos de R${preco_normal // 2}')

elif pagamento == 4: # 3x ou mais no cartão
    parcelas = int(input('Em quantas vezes deseja pagar? \n >>> '))
    valor_parcelado = preco_normal // parcelas
    print(f'O valor de cada parcela será de R${valor_parcelado + (valor_parcelado * 0.2)}') # Inclusão dos 20% de juros

