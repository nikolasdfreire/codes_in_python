'''
Elabore uma função que retorne a soma de dois números.
'''

def somar(num1, num2):
    soma = num1 + num2
    return soma

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

print(f'A soma é: {somar(n1, n2)}')