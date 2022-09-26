'''
Elabore uma função que receba um número inteiro e retorne o fatorial deste número.

'''

from math import factorial

def fatorial(num):
    print(factorial(num))

num = int(input('Digite um numero: '))
fatorial(num)