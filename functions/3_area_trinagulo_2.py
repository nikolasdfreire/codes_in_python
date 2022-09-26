'''
Escreva uma função que retorne a área de um triângulo. 
A sua função deve receber como parâmetros a base e a altura. 
Lembre que a área de um triângulo é dada pela fórmula: A=(base x altura)/2
'''

def area_tringulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input('Digite o tamanho da base do triangulo: '))
altura = float(input('Digite o tamanho da altura do triangulo: '))

print(f'A área é: {area_tringulo(base, altura)}')
