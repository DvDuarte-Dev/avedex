import json
from pathlib import Path
from src.avedex.utils import mensagem_erro


CAMINHO_PROJETO = Path(__file__).resolve().parents[2]
CAMINHO_AVES = CAMINHO_PROJETO / "data" / "aves.json"

CAMPOS_OBRIGATORIOS = [
    "id",
    "slug",
    "nome_popular",
    "nome_cientifico",
    "ordem",
    "familia",
    "dieta_tipo",
    "comprimento_cm",
    "peso_g",
    "status_conservacao",
    "indice_conservacao",
    "descricao",
    "habitat",
    "alimentacao",
    "midia",
]

CAMPOS_MIDIA = [
    "pagina_guia",
    "fotografo",
    "wikiaves_url",
    "som_url",
    "imagem_url",
]

def carregar_aves():
    try:
        with open(CAMINHO_AVES, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return dados.get("aves", [])

    except FileNotFoundError:
        mensagem_erro(
            f"Arquivo de dataset não encontrado: {CAMINHO_AVES}"
        )
        return []

    except json.JSONDecodeError:
        mensagem_erro("Erro ao ler o JSON do dataset.")
        mensagem_erro(
            "Verifique vírgulas, aspas, chaves e colchetes."
        )
        return []