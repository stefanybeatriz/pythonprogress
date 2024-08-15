'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior')
elif segundo_valor > primeiro_valor:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')

