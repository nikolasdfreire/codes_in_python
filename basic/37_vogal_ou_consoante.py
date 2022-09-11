lista_vogal = []
caractere = input('Digite um caractere: ')
if caractere in 'aeiou':
    lista_vogal.append(caractere)
    print(lista_vogal)
else:
    print(f'O caractere {caractere} não é uma vogal')


