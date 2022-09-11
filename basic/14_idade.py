nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))
if idade>=18:
    print(f'Seja bem-vindo ao nosso site {nome.strip().title()}.')
else:
    print(f'Você não pode acessar nosso site {nome.strip().title()}.')