from pathlib import Path
import re

import pymupdf
from openpyxl import Workbook

def factura_valida(datos):
    campos_obligatorios = [
        datos["numero"],
        datos["empresa"],
        datos["rut"],
        datos["fecha"],
        datos["total"],
    ]

    return all(campo is not None for campo in campos_obligatorios)

def extraer_texto_pdf(ruta_pdf):
    pdf = pymupdf.open(ruta_pdf)

    texto_completo = ""

    for pagina in pdf:
        texto_completo += pagina.get_text()

    pdf.close()

    return texto_completo


def obtener_archivos_pdf(carpeta):
    return list(Path(carpeta).glob("*.pdf"))


def convertir_monto(monto):
    if monto is None:
        return None

    return int(monto.replace(".", ""))


def extraer_datos_factura(texto):
    numero = re.search(r"N°:\s*(\d+)", texto)
    empresa = re.search(r"Empresa:\s*(.+)", texto)
    rut = re.search(r"RUT:\s*([\d.-]+)", texto)
    fecha = re.search(r"Fecha:\s*(\d{2}/\d{2}/\d{4})", texto)
    subtotal = re.search(r"Subtotal:\s*\$([\d.]+)", texto)
    iva = re.search(r"IVA:\s*\$([\d.]+)", texto)
    total = re.search(r"Total:\s*\$([\d.]+)", texto)

    return {
        "numero": numero.group(1) if numero else None,
        "empresa": empresa.group(1).strip() if empresa else None,
        "rut": rut.group(1) if rut else None,
        "fecha": fecha.group(1) if fecha else None,
        "subtotal": convertir_monto(subtotal.group(1)) if subtotal else None,
        "iva": convertir_monto(iva.group(1)) if iva else None,
        "total": convertir_monto(total.group(1)) if total else None,
    }


def crear_excel(resultados, ruta_salida):
    libro = Workbook()
    hoja = libro.active
    hoja.title = "Facturas"

    hoja.append([
        "Archivo",
        "N° Factura",
        "Empresa",
        "RUT",
        "Fecha",
        "Subtotal",
        "IVA",
        "Total"
    ])

    for resultado in resultados:
        hoja.append([
            resultado["archivo"],
            resultado["numero"],
            resultado["empresa"],
            resultado["rut"],
            resultado["fecha"],
            resultado["subtotal"],
            resultado["iva"],
            resultado["total"]
        ])

    libro.save(ruta_salida)


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