'''
Escreva uma função que receba uma lista de números
 reais como parâmetro e retorne a média destes números.
'''
def media_lista(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media



lista = []
for v in range(1, 6):
    valor = float(input(f'Digite o valor {v}: '))
    lista.append(valor)

print(media_lista(lista))