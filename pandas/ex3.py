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
display(vendas_df)
vendas_df.info()

#modificando formatação de uma coluna
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'], format='%d/%m/%Y')

#adicionando linhas
vendas_df['Dia da Venda'] = vendas_df['Data da Venda'].dt.day
vendas_df['Mês da Venda'] = vendas_df['Data da Venda'].dt.month
vendas_df['Ano da Venda'] = vendas_df['Data da Venda'].dt.year

vendas_df['Mês do Envio'] = vendas_df['Data do Envio'].dt.month
vendas_df