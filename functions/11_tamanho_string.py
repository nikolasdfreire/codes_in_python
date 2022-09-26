'''
Escreva uma função que retorna o tamanho de uma string.
'''
def tamanho_string(palavra):
    tamanho = len(palavra)
    return tamanho

palavra = str(input('Digite uma palavra: '))
print(tamanho_string(palavra))