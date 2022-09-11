
nome=input('Digite seu nome: ').strip().title()
sobrenome=input('Digite seu sobrenome: ').strip().title()
salario=float(input('Digite seu salário: '))
salario1=salario+salario*0.1  #salário com 10% de aumento
salario2=salario+salario*0.25  #salário com 25% de aumento
salario3=salario+salario*0.3  #salário com 30% de aumento
salario4=salario+salario*0.5  #salário com 50% de aumento
 
print(f'Olá, {nome} {sobrenome}')
print(f'Seu salário atual é: R$ {salario:.2f}')
print(f'Seu salário com 10% de aumento é: R$ {salario1:.2f}')
print(f'Seu salário com 25% de aumento é: R$ {salario2:.2f}')
print(f'Seu salário com 30% de aumento é: R$ {salario3:.2f}')
print(f'Seu salário com 50% de aumento é: R$ {salario4:.2f}')