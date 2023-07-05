import pandas as pd

vendas_df = pd.read_csv(r'C:\Users\Home\Desktop\pandas work\Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'C:\Users\Home\Desktop\pandas work\Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'C:\Users\Home\Desktop\pandas work\Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'C:\Users\Home\Desktop\pandas work\Contoso - Clientes.csv', sep=';')

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.rename(columns = {'E-mail': 'Email do cliente'})
#display(vendas_df)

            #media total de devolucao
total_vendido = vendas_df['Quantidade Vendida'].sum()
total_devolvido = vendas_df['Quantidade Devolvida'].sum()

media_devolvida = total_devolvido/total_vendido
#print(f'{media_devolvida:.2%}')

            #media austin de devolução
vendas_austin = vendas_df[vendas_df['ID Loja'] == 86]
total__vendas_austin = vendas_austin['Quantidade Vendida'].sum()
total_devolvido_austin = vendas_austin['Quantidade Devolvida'].sum()

media_devolvida_austin = total_devolvido_austin / total__vendas_austin
#print(f'{media_devolvida_austin:.2%}')

            #tabela Contoso europe online com devolução igual a 0.
df_contosoeuropeonline = vendas_df[vendas_df['Nome da Loja'].str.strip() == 'Loja Contoso Europe Online']

vendacontoso_devolucao0 = vendas_df[(vendas_df['ID Loja'] == 306) & (vendas_df['Quantidade Devolvida'] == 0)]
vendacontoso_devolucao0