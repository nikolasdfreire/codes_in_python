'''
Considere a tupla1 e responda as seguintes questões:



tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')



a) mostre na tela o tamanho desta tupla;

b) ordene a tupla e mostre o resultado na tela;

c) mostre na tela o número de ocorrências da string 'A';

d) mostre na tela o número de ocorrências da string 'B';

e) mostre na tela o índice da string 'X';

f) mostre na tela o último elemento da tupla1.
'''

from itertools import count


tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')

#a)
tamanho = len(tupla1)
print(tamanho)

#b)
ordenado = sorted(tupla1)
print(ordenado)

#c)
contar = tupla1.count('A')
print(contar)

#d)
contar_B = tupla1.count('B')
print(contar_B)

#e)
index_x = tupla1.index('X')
print(index_x)

#f)
print(tupla1[-1])
