'''
Escreva uma função que retorne a área de um retângulo. A sua função 
deve receber a base e a altura como parâmetros. 
Lembre que a área de um retângulo é dada pela fórmula: A=base x altura .
'''

def area_tringulo(base, altura):
    area = base * altura
    return area

base = float(input('Digite o tamanho da base do triangulo: '))
altura = float(input('Digite o tamanho da altura do triangulo: '))

print(f'A área é: {area_tringulo(base, altura)}')
