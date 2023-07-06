#TRANSFORMANDO e Baixando DICIONARIO EM DATAFRAME

import pandas as pd

vendas_df = {
    'iphone': [2000, 4500],
    'xiaomi redmi note 9': [24600, 6300],
    'samsung galaxy s20': [12000, 9800],
    'motorola moto g9': [8000, 5500],
    'huawei p30': [3000, 2200],
    'oneplus 8t': [5000, 4800],
    'google pixel 5': [4000, 3200],
    'oppo reno 4 pro': [6000, 5300],
    'vivo v20': [7000, 6500],
    'realme 7 pro': [9000, 8200],
    'lg velvet': [1500, 1200],
    'nokia 7.2': [2500, 1900],
    'sony xperia 5 ii': [1800, 1500],
    'lenovo legion phone duel': [3500, 2800],
    'asus rog phone 3': [3200, 2900],
    'blackberry key2': [1000, 800],
    'xiaomi mi 10t pro': [11000, 9600],
    'oneplus nord': [8500, 7700],
    'realme x50 pro': [7500, 6200],
    'oppo find x2 pro': [4800, 4500],
    'vivo x50 pro': [5500, 5200],
    'google pixel 4a': [2200, 1900],
    'samsung galaxy a51': [10000, 9200],
    'motorola razr': [1300, 1000],
    'iphone se (2020)': [6000, 5700],
    'xiaomi mi 11': [7500, 7100],
    'samsung galaxy note 20 ultra': [9000, 8600],
    'huawei mate 40 pro': [4200, 4000],
    'nokia 8.3': [2800, 2400],
    'realme 6 pro': [5800, 5400],
    'oneplus 8 pro': [6700, 6400],
    'asus zenfone 7 pro': [3200, 3000],
    'vivo nex 3': [2500, 2200],
    'lg g8x thinq': [1800, 1600],
    'sony xperia 1 ii': [2100, 1900],
    'oppo reno 3 pro': [5500, 5100],
    'google pixel 4 xl': [3200, 2900],
    'samsung galaxy s10': [7800, 7400],
    'motorola edge plus': [4000, 3800],
    'iphone 11 pro': [4800, 4600],
    'xiaomi mi note 10': [3800, 3500],
    'realme x2 pro': [5200, 4900],
    'huawei p40 pro': [2700, 2500],
    'oneplus 7t pro': [2900, 2700],
    'vivo iqoo neo 855': [1700, 1500],
}

novo_dic_df = pd.DataFrame.from_dict(vendas_df, orient='index')
novo_dic_df = novo_dic_df.rename(columns={0:'Vendas 2022', 1: 'Vendas 2023'})
display(novo_dic_df)

novo_dic_df.to_csv(r'C:\Users\Home\Desktop\pandas work\teste\teste 2 soe.csv', sep=';')