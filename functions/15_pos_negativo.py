'''
verifica se o numero é positivo ou negativo
'''

def negativo_positivo(num):
    if num > 0:
        print(f'O numero {num} é positivo')
    else:
        print(f'O numero {num} é negativo')

num = int(input('Numero: '))
negativo_positivo(num)