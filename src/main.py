from excel_writer import crear_excel
from invoice_parser import (
    extraer_datos_factura,
    factura_valida,
    obtener_campos_faltantes,
)
from pdf_reader import extraer_texto_pdf, obtener_archivos_pdf


def main():
    archivos_pdf = obtener_archivos_pdf("input")

    if not archivos_pdf:
        print("No se encontraron archivos PDF en la carpeta input.")
        return

    resultados = []
    ignorados = 0

    for archivo_pdf in archivos_pdf:
        texto = extraer_texto_pdf(archivo_pdf)

        if texto is None:
            ignorados += 1
            continue

        datos = extraer_datos_factura(texto)

        if not factura_valida(datos):
            campos_faltantes = obtener_campos_faltantes(datos)

            print(
                f"✗ {archivo_pdf.name} - "
                f"faltan campos: {', '.join(campos_faltantes)}"
            )

            ignorados += 1
            continue

        datos["archivo"] = archivo_pdf.name
        resultados.append(datos)

        print(f"✓ {archivo_pdf.name}")

    excel_generado = crear_excel(
        resultados,
        "output/resultados.xlsx"
    )

    print()
    print(f"Facturas procesadas: {len(resultados)}")
    print(f"Documentos ignorados: {ignorados}")

    if excel_generado:
        print("Excel generado correctamente.")


if __name__ == "__main__":
    main()