'''
Considere a lista a seguir, que apresenta dados 
referentes a série temporal de 1900 a 2020. Faça o que se pede:

a) Crie uma lista  que armazene os 20 primeiros anos da série;

b) Crie uma lista que armazene os anos de 1937 a 1969;

c) Crie uma lista que armazene os anos de 2010 a 2020;

d) Crie uma lista que armazene o último ano da série;

e) Apresente a série temporal de 10 em 10 anos.

'''

#a)
lista = []
for ano in range(1900, 2021):
    lista.append(ano)
    lista2 = lista[0:21]
print(lista2)


#b)
lista3 = []
for ano in range(1900, 2021):
    lista3.append(ano)
    lista4 = lista3[37:70]
print(lista4)

#c)
lista5 = []
for ano in range(1900, 2021):
    lista5.append(ano)
    lista6 = lista5[-11:]
print(lista6)

#d)
lista7 = []
for ano in range(1900, 2021):
    lista7.append(ano)
    lista8 = lista7[-1:]
print(lista8)

#e)
lista9 = []
for ano in range(1900, 2021):
    lista9.append(ano)
    lista10 = lista7[::10]
print(lista10)


