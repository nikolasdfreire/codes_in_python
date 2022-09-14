lista_par = []
lista_impar = []
num = 1
while num:
    num = int(input('Digite um valor: '))
    if num%2 == 0:
        lista_par.append(num)
    elif num%2==1:
        lista_impar.append(num)
    if num < 0:
        print('Valor negativo')
    elif num == 0:
        print('Valor nulo')
print(f'par: {len(lista_par)}')
print(f'impar: {len(lista_impar)}')
    

