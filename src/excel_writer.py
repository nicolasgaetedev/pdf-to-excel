from openpyxl import Workbook


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