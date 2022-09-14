'''
Escreva um programa para checar se um determinado número é primo ou não.

Lembrete: um número primo pode ser dividido por apenas dois números, quais sejam: ele mesmo e o número um.
'''
num = int(input('Digite um numero: '))
if num > 1:
    for i in range(2, num):
        if num%i==0:
            print(f'O numero {num} não é primo')
            break
    else:
        print(f'O numero {num} é primo')
else:
    print(f'O numero {num} não é primo')

