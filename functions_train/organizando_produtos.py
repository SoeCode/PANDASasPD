#criar uma função para o usuario escolher se quer trabalhar com a lista toda minuscula ou toda maiuscula.

def padronizar_lista(lista_celular, padrao='m'):
    for i, celular in enumerate(lista_celular):
        celular = celular.replace('  ', ' ')
        celular = celular.strip()
        if padrao == 'm':
            celular = celular.casefold()
        elif padrao == 'M':
            celular = celular.upper()
        lista_celular[i] = celular
    return lista_celular

            
soe_celulares = [
    'Xiaomi  Mi 11',
    'Xiaomi Redmi Note 10 Pro',
    'Xiaomi Poco X3 Pro',
    'Xiaomi Mi 10T Pro',
    'Xiaomi Redmi 9',
    'Xiaomi  Mi 11 Lite',
    'Xiaomi Redmi Note 9S',
    'Xiaomi Poco X3 NFC',
    'Xiaomi Mi 10',
    'Xiaomi Redmi Note 8 Pro',
    'Xiaomi Mi 11 Ultra',
    'Xiaomi Redmi Note 10',
    'Xiaomi Mi 9T',
    'Xiaomi Poco M3',
    'Xiaomi Mi Mix 3',
    'Xiaomi Redmi Note 7',
    'Xiaomi Mi 9 SE',
    'Xiaomi Poco F3',
    'Xiaomi  Mi 11i',
    'Xiaomi Redmi K40',
    'Samsung Galaxy S21',
    'Samsung Galaxy Note 20 Ultra',
    'Samsung  Galaxy A52',
    'Samsung Galaxy S20 FE',
    'Samsung Galaxy M51',
    'Samsung Galaxy A32',
    'Samsung  Galaxy S10',
    'Samsung Galaxy Note 10',
    'Samsung Galaxy Z Flip',
    'Samsung  Galaxy A72'
]

padronizar_lista(soe_celulares, 'M')
for i in soe_celulares:
    print(i)