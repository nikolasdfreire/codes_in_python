'''
Considere um número inteiro positivo n especificado pelo usuário. Elabore um programa que calcule e mostre na tela:
A soma dos n primeiros números inteiros não-nulos (1+2+3+ ... +n) ;
A soma dos n primeiros números pares;
A soma dos n primeiros números ímpares.

'''

valor = int(input('Digite um valor: '))
soma = 0
soma_par = 0
soma_impar = 0
for numero in range(1, valor+1):
    if numero%2==0:
        soma_par += numero
    elif numero%2==1:
        soma_impar+=numero
    
    soma+=numero
    
print(f'A soma dos numeros pares entre 1 e {valor} é: {soma_par}')
print(f'A soma dos numeros impares entre 1 e {valor} é: {soma_impar}')
print(f'A soma de todos os numero entre 1 e {valor} é: {soma}') 