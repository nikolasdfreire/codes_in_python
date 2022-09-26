'''
Escreva um programa que pesquise um determinado valor em uma lista. 
Sua função deve ter como parâmetros a lista e o valor a ser verificado. 
Caso o valor faça parte da lista informada retorne True e False, caso contrário.

'''

def procura_lista(lista, valor):
    if valor in lista:
        return True
    else:
        return False

lista = []
for v in range(0, 6):
    _valor = input(f'Digite um valor {v} para a lista: ')
    lista.append(_valor)

valor = input('Digite um valor para verificar se tem na lista: ')
print(procura_lista(lista, valor))