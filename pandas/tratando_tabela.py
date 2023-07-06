#Tratando tabela usando dois metodos: PANDAS e OPENPYXL
# pandas
import pandas as pd

#importar a tabela para pandas e criar um dataframe

produto_df = pd.read_excel('Produtos -  now.xlsx')
#display(produto_df)

#Atualizar o multiplicador
produto_df.loc[produto_df['Tipo'] == 'Serviço', 'Multiplicador Imposto'] = 1.5

#Fazer a conta do do Preço Base Reais
produto_df['Preço Base Reais'] = produto_df['Preço Base Original'] * produto_df['Multiplicador Imposto']
display(produto_df)

#produto_df.to_excel(r'C:\Users\Home\Desktop\pandas work\teste\Teste 3 soe.xlsx', index=False)
#||||
#Usando Openpyxl
from openpyxl import workbook, load_workbook

planilha = load_workbook('Produtos -  now.xlsx')

aba_ativa = planilha.active

for celula in aba_ativa['C']:
    if celula.value == 'Serviço':
        linha = celula.row
        aba_ativa[f'D{linha}'] = 1.5
        
#planilha.save(r'C:\Users\Home\Desktop\pandas work\teste\Teste 4 soeOpenpy.xlsx')