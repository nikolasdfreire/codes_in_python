lista_compras=[
    {'nome':'feijão','preco':9.79},
    {'nome':'arroz','preco':3.45},
    {'nome':'carne','preco':20.93},
    {'nome':'macarrão','preco':2.99},
    {'nome':'vinagre','preco':2.25},
    {'nome':'pimenta','preco':1.27},
    {'nome':'batata','preco':5.67},
    {'nome':'leite','preco':12},
    {'nome':'manteiga','preco':7.99},
    {'nome':'margarina','preco':2.5},
    {'nome':'cenoura','preco':3.55},
    {'nome':'sabão','preco':4.79},
    {'nome':'chá','preco':3.45},
    {'nome':'morango','preco':17.8},
    {'nome':'soja','preco':20.2},
    {'nome':'goiaba','preco':3.45},
    {'nome':'melão','preco':5.12},
]
#quando eh um dicionario temos que fazer assim!
maior_valor = max(lista_compras, key=lambda produto:produto['preco'])
menor_valor = min(lista_compras, key=lambda produto:produto['preco'])
print(f"Produto mais caro: {maior_valor['nome'].title()} - R$ {maior_valor['preco']:.2f}" )
print(f"Produto mais barato: {menor_valor['nome'].title()} - R$ {menor_valor['preco']:.2f}")
