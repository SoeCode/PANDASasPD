def preco_final(preco, **adicionais):
    '''Atualizar preço podendo adicionar keywords arguments multiplas

    Parameters:
        preco do produto, modificações adicionais ilimitadas

    Return:
        preço do produto tratado com os adicionais
    
    '''

    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_estendida' in adicionais:
        preco += adicionais['garantia_estendida']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

print(preco_final(200, desconto=0.2, imposto=0.1))