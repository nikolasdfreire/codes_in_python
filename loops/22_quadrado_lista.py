lista = []

for numero in range(1, 6):
    valor = int(input(f'Digite o numero da posicao {numero}: '))
    lista.append(valor*valor)

print(lista)