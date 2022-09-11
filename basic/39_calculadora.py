operacao = input('Digite a operação: ')
if operacao in "+-*/":
    if operacao == '+':
        num1 = float(input('Numero 1 = '))
        num2 = float(input('Numero 2 = '))
        soma = num1 + num2
        print(soma)
    elif operacao == '-':
        num1 = float(input('Numero 1 = '))
        num2 = float(input('Numero 2 = '))
        soma = num1 - num2
        print(soma)
    elif operacao == '*':
        num1 = float(input('Numero 1 = '))
        num2 = float(input('Numero 2 = '))
        soma = num1 * num2
        print(soma)
    elif operacao == '/':
        num1 = float(input('Numero 1 = '))
        num2 = float(input('Numero 2 = '))
        if num1 == 0 or num2 == 0:
            print('O número 0 é inválido')
        else:
            soma = num1 / num2
            print(soma)
else:
    print('Operação inválida')

