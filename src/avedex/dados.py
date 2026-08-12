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

def validar_ave(ave):
    problemas = []

    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in ave:
            problemas.append(
                f"campo obrigatório ausente: {campo}"
            )

    midia = ave.get("midia")

    if not isinstance(midia, dict):
        problemas.append(
            "campo 'midia' ausente ou inválido"
        )
    else:
        for campo in CAMPOS_MIDIA:
            if campo not in midia:
                problemas.append(
                    f"campo de mídia ausente: {campo}"
                )

    if not isinstance(ave.get("comprimento_cm"), (int, float)):
        problemas.append(
            "comprimento_cm deveria ser número"
        )

    if not isinstance(ave.get("peso_g"), (int, float)):
        problemas.append(
            "peso_g deveria ser número"
        )

    if not ave.get("nome_popular"):
        problemas.append(
            "nome_popular não pode ficar vazio"
        )

    return problemas

def validar_dataset(aves):
    problemas = []
    ids_vistos = set()

    for ave in aves:
        problemas_ave = validar_ave(ave)

        for problema in problemas_ave:
            problemas.append(
                f"Ave {ave.get('id', '?')}: {problema}"
            )

        id_ave = ave.get("id")

        if id_ave in ids_vistos:
            problemas.append(
                f"ID duplicado: {id_ave}"
            )

        ids_vistos.add(id_ave)

    return problemas

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