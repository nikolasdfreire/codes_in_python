'''
18.1 Crie um script para iterar no dicionário abaixo e 
mostrar na tela todas as suas chaves, uma a uma.

18.2 Crie um script para iterar no dicionário produto1 e 
mostrar na tela todos os seus valores, um a um.

18.3 Crie um script para iterar no dicionário 
produto1 e mostrar chave,valor na tela.

'''

produto1={
    'nome':'produto1',
    'tipo':'categoriaA',
    'valor':'50.5',
    'fornecedor':'ABCD',
}

#18.1
for chave in produto1:
    print(chave)

#18.2
for chave in produto1:
    print(produto1[chave])

#18.3
for chave, valor in produto1.items():
    print(chave, valor)


