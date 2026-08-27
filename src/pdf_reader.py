from pathlib import Path

import pymupdf


def extraer_texto_pdf(ruta_pdf):
    pdf = pymupdf.open(ruta_pdf)

    texto_completo = ""

    for pagina in pdf:
        texto_completo += pagina.get_text()

    pdf.close()

    return texto_completo


def obtener_archivos_pdf(carpeta):
    return list(Path(carpeta).glob("*.pdf"))