from pathlib import Path
from urllib.parse import urlparse

from src.avedex.utils import mensagem_aviso


CAMINHO_PROJETO = Path(__file__).resolve().parents[2]

PASTA_CACHE = CAMINHO_PROJETO / "cache_midias"

EXTENSOES_PADRAO = {
    "imagem": ".jpg",
    "som": ".mp3",
}

EXTENSOES_PERMITIDAS = {
    "imagem": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "som": {".mp3", ".wav", ".ogg"},
}


def obter_url_midia(ave, tipo):
    midia = ave.get("midia", {})

    if not isinstance(midia, dict):
        return ""

    if tipo == "imagem":
        campo = "imagem_url"
    else:
        campo = "som_url"

    return str(
        midia.get(campo, "")
    ).strip()


def descobrir_extensao(url, tipo):
    caminho_url = urlparse(url).path

    extensao = Path(
        caminho_url
    ).suffix.lower()

    if extensao in EXTENSOES_PERMITIDAS[tipo]:
        return extensao

    return EXTENSOES_PADRAO[tipo]


def criar_caminho_cache(ave, tipo, url):
    nome = ave.get(
        "slug",
        ave.get("nome_popular", "ave")
    )

    nome = str(nome).lower().replace(" ", "-")

    extensao = descobrir_extensao(
        url,
        tipo
    )

    return (
        PASTA_CACHE
        / f"{nome}_{tipo}{extensao}"
    )


def baixar_arquivo(url, caminho_destino):
    try:
        import requests
    except ImportError:
        mensagem_aviso(
            "A biblioteca requests não está instalada."
        )
        return False

    try:
        caminho_destino.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        resposta = requests.get(
            url,
            timeout=20
        )

        resposta.raise_for_status()

        caminho_destino.write_bytes(
            resposta.content
        )

        return True

    except requests.RequestException as erro:
        mensagem_aviso(
            f"Não foi possível baixar a mídia: {erro}"
        )
        return False