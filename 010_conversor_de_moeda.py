# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Valor do dólar: R$5,00 (mar. 2024)
reais = float(input('Digite a quantidade de dinheiro que você tem mãos: \nR$'))
dolar = float(reais / 5)

print(f'Você pode comprar {dolar} dólares com {reais} reais')
