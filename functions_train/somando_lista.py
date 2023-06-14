#básico de uma function somando uma itens de uma lista
def soma(lista):
    soma=0
    for i in lista:
        soma += i
    return soma


lista = [10,30,12,50,24,43,12,67,32,55,11,10,10,100]
total_soma_lista = soma(lista)
print(total_soma_lista)