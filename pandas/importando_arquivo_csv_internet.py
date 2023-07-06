#Importando E TRATANDO ARQUIVO CSV DA NET
import pandas as pd
import requests
import io

url = 'http://portalweb.cooxupe.com.br:8080/portal/precohistoricocafe_2.jsp?d-3496238-e=2&6578706f7274=1'
conteudo_url = requests.get(url).content
arquivo = io.StringIO(conteudo_url.decode('latin1'))

produtos_df = pd.read_csv(arquivo, sep='\t')
display(produtos_df)