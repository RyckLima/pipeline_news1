# Pipeline de Notícias: Geopolítica & Relações Internacionais 🌍
Este projeto é um pipeline de dados (ETL) automatizado que extrai notícias globais via API, filtra conteúdos específicos sobre geopolítica e armazena os dados tratados em um banco de dados SQL para análise futura.

🚀 Arquitetura do Projeto
O sistema foi construído seguindo princípios de modularização e encapsulamento, dividido em três etapas principais:

Extração (src/extracao.py): Consome dados da NewsAPI utilizando filtros de busca customizados.

Transformação (src/limpeza_dados.py): Utiliza a biblioteca Pandas para normalizar o JSON, remover duplicatas, tratar valores nulos e aplicar uma filtragem híbrida baseada em palavras-chave estratégicas (ex: OTAN, BRICS, soberania).

Carga (src/load.py): Utiliza o SQLAlchemy como engine para criar a estrutura das tabelas e realizar o carregamento dos dados em um banco SQLite local.

🛠️ Tecnologias Utilizadas
Python 3.13+

Pandas: Manipulação e limpeza de dados.

SQLAlchemy: Engine de conexão e gerenciamento de banco de dados SQL.

Requests: Consumo de API REST.

Python-dotenv: Gerenciamento de variáveis de ambiente (API Keys).