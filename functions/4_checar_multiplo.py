'''
Escreva uma função que verifique se um número 
é múltiplo do outro e retorne um valor lógico.

def checar_multiplo(numero1,numero2):
    if numero1%numero2==0:
        return True
    else:
        return False
'''

def checar_multiplo(num1, num2):
    multiplo = num1%num2==0
    return multiplo

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

print(checar_multiplo(n1, n2))