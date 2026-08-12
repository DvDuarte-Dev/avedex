import json
from pathlib import Path
from src.avedex.utils import mensagem_erro


CAMINHO_PROJETO = Path(__file__).resolve().parents[2]
CAMINHO_AVES = CAMINHO_PROJETO / "data" / "aves.json"


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