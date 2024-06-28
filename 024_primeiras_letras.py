# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome de uma cidade: \n >> ')).upper().split()
# Já deixei tudo em maíusculo e separado na mesma linha de código com as funções upper e split

# Se o nome da cidade começar com Santo...
if cidade[0] == 'SANTO':
    print('O nome desta cidade começa com Santo')
else:
    print('O nome desta cidade não começa com Santo')

