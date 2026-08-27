from pathlib import Path

import pymupdf


def extraer_texto_pdf(ruta_pdf):
    try:
        pdf = pymupdf.open(ruta_pdf)

        texto_completo = ""

        for pagina in pdf:
            texto_completo += pagina.get_text()

        pdf.close()

        return texto_completo

    except Exception as error:
        print(f"✗ Error al leer {ruta_pdf.name}: {error}")
        return None


def obtener_archivos_pdf(carpeta):
    return list(Path(carpeta).glob("*.pdf"))