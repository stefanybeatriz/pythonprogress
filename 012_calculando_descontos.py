# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto: \nR$'))
desconto = preco - (preco * 0.05)

print(f'O preço deste produto com 5% de desconto equivale a: R${desconto}')
