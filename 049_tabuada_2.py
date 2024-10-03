# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

numero = int(input('Digite o número que deseja saber a tabuada: '))

for c in range(1, 11):
    print(f'{c} x {numero} = {c * numero}')

