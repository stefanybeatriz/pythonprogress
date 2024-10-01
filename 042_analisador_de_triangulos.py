'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

print('Analisador de Triângulos \nDigite o comprimento das 3 retas: ')

# Obtendo as retas do triângulo
a = float(input('Reta A: '))
b = float(input('Reta B: '))
c = float(input('Reta C: '))

# Como saber se elas formam um triângulo
if a < b + c and b < a + c and c < b + a:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')
    exit()
    
# Como saber o tipo de triângulo:
if a == b == c:
    print('Este triângulo é EQUILÁTERO: tem todos os lados iguais!')
elif a == b or a == c or b == c:
    print('Este triângulo é ISÓSCELES: tem 2 lados iguais e 1 diferente!')
elif a != b != c !=a:
    print('Este triângulo é ESCALENO: tem todos os lados de tamanhos diferentes!')
