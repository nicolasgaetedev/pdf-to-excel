import pymupdf


def extraer_texto_pdf(ruta_pdf):
    pdf = pymupdf.open(ruta_pdf)

    texto_completo = ""

    for pagina in pdf:
        texto_completo += pagina.get_text()

    pdf.close()

    return texto_completo


def main():
    ruta_pdf = "input/prueba.pdf"

    texto = extraer_texto_pdf(ruta_pdf)

    print(texto)


if __name__ == "__main__":
    main()