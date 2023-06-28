import pandas as pd
import pprint

from dic import dicionario_vimeo
#for chave in dicionario_vimeo:
    #print(chave)
lista_info = dicionario_vimeo['data']
chave = []


def achar_link(dicionario):
    link = None
    if dicionario['rendition'] == '540p':
        link = dicionario['link']
    elif dicionario['rendition'] == '720p':
        link = dicionario['link']
    elif dicionario['rendition'] == '1080p':
        link = dicionario['link']
    return link


for dicionario_videos in lista_info:
    uri = dicionario_videos['uri']
    nome = dicionario_videos['name']
    duracao = dicionario_videos['duration']
    info_download = dicionario_videos['download']
    
    for dicionario_download in info_download:
        achar_link(dicionario_download)
        
    chave.append({
        "url" : uri,
        "nome" : nome,
        "duracao" : duracao,
        "link540p" : link540p,
        "link720p" : link720p,
        "link1080p" : link1080p
    })

# pprint.pprint(dicionario_vimeo)
# tabela = pd.DataFrame(chave)
# print(tabela)
#a
