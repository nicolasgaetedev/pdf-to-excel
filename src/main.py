from excel_writer import crear_excel
from invoice_parser import extraer_datos_factura, factura_valida
from pdf_reader import extraer_texto_pdf, obtener_archivos_pdf


def main():
    archivos_pdf = obtener_archivos_pdf("input")

    resultados = []
    ignorados = 0

    for archivo_pdf in archivos_pdf:
        texto = extraer_texto_pdf(archivo_pdf)
        datos = extraer_datos_factura(texto)

        if not factura_valida(datos):
            print(f"✗ {archivo_pdf.name} - formato no reconocido")
            ignorados += 1
            continue

        datos["archivo"] = archivo_pdf.name
        resultados.append(datos)

        print(f"✓ {archivo_pdf.name}")

    crear_excel(resultados, "output/resultados.xlsx")

    print()
    print(f"Facturas procesadas: {len(resultados)}")
    print(f"Documentos ignorados: {ignorados}")
    print("Excel generado correctamente.")


if __name__ == "__main__":
    main()