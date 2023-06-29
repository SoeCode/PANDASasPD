lista_vendas = [
    ('celular', 43500, 57200),
    ('fones', 38750, 50250),
    ('relógio', 51600, 42900),
    ('pulseira', 35400, 48750),
    ('tablet', 52100, 40900),
    ('notebook', 56750, 44300),
    ('smartwatch', 47300, 39450),
    ('câmera', 44800, 56350),
    ('televisor', 52250, 35800),
    ('caixa de som', 40150, 59200)
]


vendas22 = [vendas22 for item, vendas22, vendas23 in lista_vendas]

#maior valor de venda 2022:
print(f'quantidade mais vendido em 2022: {max(vendas22)}')

vendasprodutos22 = [(vendas22, item) for item, vendas22, vendas23 in lista_vendas]

print(f'produto e quant. mais vendido em 2022: {max(vendasprodutos22)}')

#a