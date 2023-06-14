# function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto,
#dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.
def calcular_imposto(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco


preco = float(input("preço: "))
custo = float(input("custo: "))
lucro = float(input("lucro: "))
imposto = calcular_imposto(preco, custo, lucro)


print(f' O valor do imposto em porcentagem foi de {imposto:.1%}')