from sqlalchemy import create_engine , text
from limpeza_dados import df_news4
from sqlalchemy.exc import IntegrityError

path_data = 'sqlite:///../data/noticias.db'
engine = create_engine(path_data)
query_create_table = """
CREATE TABLE IF NOT EXISTS noticias_geopolitica (
    url TEXT PRIMARY KEY,
    title TEXT,
    author TEXT,
    publishedAt TIMESTAMP,
    content TEXT
)
"""

# Abrindo a "ponte" e executando o comando
with engine.connect() as conexao:
    conexao.execute(text(query_create_table))

#Onde transformo de dataframe para SQL e mando para nosso banco de dados.
#aqui tem o nome da tabela, o motor que usei, se eu quero escolher entre replace ou append, e para tirar os indices do panda
try:
    df_news4.to_sql('noticias_geopolitica', con=engine, if_exists='append', index=False)
    print("Dados inseridos com sucesso.")
except IntegrityError:
    print("Aviso: Algumas URLs já existiam no banco e foram ignoradas.")