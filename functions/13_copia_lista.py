''''
Escreva uma função que faça uma cópia de uma lista.


'''

def copiar_lista(lista):
    copia=[]
    if type(lista)==list:
        if len(lista)>0:
            for elemento in lista:
                copia.append(elemento)
            return copia
        else:
            copia

print(copiar_lista([1,2]))