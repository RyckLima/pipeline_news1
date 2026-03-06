from src.extracao import extrair
from src.limpeza_dados import limpar
from src.load import subir_dados

if __name__ == "__main__":
    termos = (
            'geopolitics|diplomacy|NATO|OTAN|BRICS|sanctions|embargo|'
            'border|fronteira|treaty|acordo|summit|cúpula|foreign policy|'
            'sovereignty|soberania|unilateral|multilateral|hegemony|'
            'territory|conflict|conflito|warfare|embassy|embaixada|'
            'intelligence|espionagem|defense|defesa|geostrategy'
        )

    dados_brutos = extrair ()
    df = limpar(dados_brutos  , termos)
    subir_dados(df)
