'''
Verifique se uma lista é vazia ou não.
 Caso a lista seja vazia, mostre True na tela, caso contrário False.
'''

lista = []
print(bool(lista))

lista1 = [1, 3]
print(bool(lista1))

#outra forma
lista2 = [1]
if len(lista2) == 0:
    print('Lista vazia')
elif len(lista2) > 0:
    print('Lista com valores')
