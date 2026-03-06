import pandas as pd
from src.extracao import extrair

def limpar (dados, termos):

    #Os dados do source vieram aninhados (um dicionário dentro do outro.), então para transformar em um df usamod json_normalize
    df = pd.json_normalize(dados)

    #remoçao de colunas desnecessárias
    df_news2 = df.drop(columns = ['urlToImage' , 'source.id' , 'description'])

    #case é parametro para maiusculos e minusculos, eu estou aceitando ambos e na para valor vazio.
    filtros_titulo = df_news2['title'].str.contains(termos , case = False , na = False)
    filtros_conteudo = df_news2['content'].str.contains(termos , case = False , na = False)

    #filtragem híbrida:
    df_news3 = df_news2[filtros_titulo|filtros_conteudo]

    #limpeza de duplicatas.
    df_news4 = df_news3.drop_duplicates().copy()

    #conversão para objeto datatime na coluna de publicação:
    df_news4['publishedAt'] = pd.to_datetime(df_news4['publishedAt'])

    #Tratamento de nulos (por tipo):

    regras = {
        'author': 'Unknown',
    }

    df_news4.fillna(value=regras, inplace=True)

    return df_news4

if __name__ == '__main__':
    print('Limpando dados...')
    #filtrar linhas para garantir que o conteúdo seja de geopolítica. Utilizando máscara booleana
    termos = (
        'geopolitics|diplomacy|NATO|OTAN|BRICS|sanctions|embargo|'
        'border|fronteira|treaty|acordo|summit|cúpula|foreign policy|'
        'sovereignty|soberania|unilateral|multilateral|hegemony|'
        'territory|conflict|conflito|warfare|embassy|embaixada|'
        'intelligence|espionagem|defense|defesa|geostrategy'
    )
    print(limpar(extrair() , termos))




