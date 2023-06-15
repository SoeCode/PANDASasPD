#criar uma funcao para filtrar apenas os emails desejado.
#1passo criar funcao e argumentos(parametros):
#2passo criar nova lista filtrada vazia.
#3passo percorrer toda lista e verificar se o provedor do email esta no item que esta sendo percorrido.
#4passo adicionar o provedor desejado na lista filtrada e retornar o valor.

def filtrar_email(lista_email, provedor_do_email):
    lista_filtrada = []
    for item in lista_email:
        if provedor_do_email in item:
            lista_filtrada.append(item)
    return lista_filtrada

lista_emails = [
    'joao.silva@gmail.com',
    'maria.rodrigues@gmail.com',
    'pedro.santos@gmail.com',
    'ana.pereira@gmail.com',
    'carlos.almeida@gmail.com',
    'juliana.martins@gmail.com',
    'rodrigo.oliveira@gmail.com',
    'patricia.sousa@gmail.com',
    'lucas.melo@gmail.com',
    'fernanda.ferreira@gmail.com',
    'luisa.andrade@ig.com',
    'andre.rocha@ig.com',
    'sabrina.menezes@ig.com',
    'ricardo.souza@ig.com',
    'gabriela.ribeiro@hotmail.com',
    'marcos.santana@hotmail.com',
    'andreia.lima@hotmail.com',
    'rafael.mendes@hotmail.com',
    'carolina.castro@hotmail.com',
    'raquel.alves@outlook.com',
    'hugo.pinto@outlook.com',
    'camila.silveira@outlook.com',
    'felipe.nogueira@outlook.com',
    'jessica.pereira@outlook.com',
    'bruno.oliveira@outlook.com'
]

lista_filtrada = filtrar_email(lista_emails, 'gmail')
print(f'Os emails com o filtro selecionados são: ')
for item in lista_filtrada:
    print(item)