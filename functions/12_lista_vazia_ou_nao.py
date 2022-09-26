'''
Escreva uma função que retorna o tamanho de uma string.
'''

def verifica_lista(lista):
    if len(lista) == 0:
        return True
    else:
        return False


lista = [1, 2, 3]
lista1 = []

print(verifica_lista(lista))
print(verifica_lista(lista1))