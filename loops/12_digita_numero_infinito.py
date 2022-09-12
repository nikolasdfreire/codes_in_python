num = 0
soma = 0
qtd_num = 0
while num <= 10:
    num = int(input('Digite um numero entre 0 e 10: '))
    soma += num #aqui eu somo os numeos 
    qtd_num += 1 #aqui eu adiciono um numero am mais 
    if num > 10:
        print('Você digitou um valor inválido')
        soma -= num
        qtd_num -= 1
        print(f'soma = {soma}')
        print(f'A quantidade de numeros foi {qtd_num}')
        break
