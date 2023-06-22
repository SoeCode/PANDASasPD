
def somar_numeros(*numeros):
    '''Somar números com múltiplos parametros

    Parameters:
        quantidade infinita de números
    Return:
        soma dos números
    '''
    
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

print(somar_numeros(10,20,30,5,10))

