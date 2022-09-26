'''
Escreva uma função que verifique se duas listas possuem ao menos 
um elemento em comum, retornando True em caso positivo.
'''

def verifica_lista(lista1, lista2):
    for elemento in lista1:
        for elemento1 in lista2:
            if elemento == elemento1:
                return True
    return False

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 4, 8, 9, 10]
print(verifica_lista(lista1, lista2))