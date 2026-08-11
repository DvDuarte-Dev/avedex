import json
from pathlib import Path


CAMINHO_PROJETO = Path(__file__).resolve().parents[2]
CAMINHO_AVES = CAMINHO_PROJETO / "data" / "aves.json"


def carregar_aves():
    with open(CAMINHO_AVES, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados.get("aves", [])