meta = 600
lista_produtos = [
    'Arroz',
    'Feijão',
    'Macarrão',
    'Óleo de Soja',
    'Açúcar',
    'Café',
    'Leite',
    'Pão',
    'Carne',
    'Frango',
    'Peixe',
    'Legumes'
]

lista_vendas = [
    550,
    700,
    400,
    800,
    600,
    450,
    550,
    350,
    900,
    650,
    500,
    700
]

bateu_a_meta = [produto for i, produto in enumerate(lista_produtos) if lista_vendas[i] > meta]
print(f' Produtos que ficaram acima da meta: {bateu_a_meta}')