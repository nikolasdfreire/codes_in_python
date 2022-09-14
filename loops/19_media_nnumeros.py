soma = 0
for valor in range(1, 6):
    valor = int(input(f'Digite um valor {valor}: '))
    soma += valor
media = soma / 5
print(media)