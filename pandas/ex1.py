import pandas as pd

vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv('Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv('Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv('Contoso - Clientes.csv', sep=';')

# display(vendas_df)
# display(produtos_df)
# display(lojas_df)
# display(clientes_df)

#reestruturando tabela
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

#juntando colunas mais importantes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')

#renomeando colunas
vendas_df = vendas_df.rename(columns = {'E-mail': 'Email do cliente'})

#filtrando maior comprador por tabela e por grafico
frequencia_clientes = vendas_df['Email do cliente'].value_counts()
#frequencia_clientes[:5].plot(figsize = (15,5))

#criando novo dataframe para loja mais vendida
vendas_lojas = vendas_df.groupby('Nome da Loja')['Quantidade Vendida'].sum()
#vendas_lojas

#ordenando do maior para o menor em quantidade de vendas
vendas_lojas = vendas_lojas.sort_values(ascending=False)
#vendas_lojas

#maior e melhor loja
maior_valor = vendas_lojas.max()
melhor_loja = vendas_lojas.idxmax()