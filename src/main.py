from pathlib import Path

import pymupdf
from openpyxl import Workbook


def extraer_texto_pdf(ruta_pdf):
    pdf = pymupdf.open(ruta_pdf)

    texto_completo = ""

    for pagina in pdf:
        texto_completo += pagina.get_text()

    cantidad_paginas = len(pdf)

    pdf.close()

    return texto_completo, cantidad_paginas


def obtener_archivos_pdf(carpeta):
    return list(Path(carpeta).glob("*.pdf"))


def crear_excel(datos, ruta_salida):
    libro = Workbook()
    hoja = libro.active
    hoja.title = "Resultados"

    hoja.append(["Archivo", "Páginas", "Caracteres extraídos"])

    for dato in datos:
        hoja.append([
            dato["archivo"],
            dato["paginas"],
            dato["caracteres"]
        ])

    libro.save(ruta_salida)


def main():
    archivos_pdf = obtener_archivos_pdf("input")

    resultados = []

    for archivo_pdf in archivos_pdf:
        texto, cantidad_paginas = extraer_texto_pdf(archivo_pdf)

        resultado = {
            "archivo": archivo_pdf.name,
            "paginas": cantidad_paginas,
            "caracteres": len(texto)
        }

        resultados.append(resultado)

    crear_excel(resultados, "output/resultados.xlsx")

    print(f"PDF procesados: {len(resultados)}")
    print("Excel generado: output/resultados.xlsx")


if __name__ == "__main__":
    main()