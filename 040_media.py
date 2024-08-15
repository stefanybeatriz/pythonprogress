'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

prova1 = float(input('Nota da P1: '))
prova2 = float(input('Nota da P2: '))
media = (prova1 + prova2) // 2

print(f'Sua média: {media} \n '
      'Status: ')

if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')

