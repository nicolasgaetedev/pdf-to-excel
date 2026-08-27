from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


facturas = [
    {
        "archivo": "factura_1001.pdf",
        "numero": "1001",
        "empresa": "Comercial Andes SpA",
        "rut": "76.123.456-7",
        "fecha": "27/08/2026",
        "subtotal": "$100.000",
        "iva": "$19.000",
        "total": "$119.000",
    },
    {
        "archivo": "factura_1002.pdf",
        "numero": "1002",
        "empresa": "Servicios del Pacifico Ltda.",
        "rut": "77.987.654-3",
        "fecha": "26/08/2026",
        "subtotal": "$250.000",
        "iva": "$47.500",
        "total": "$297.500",
    },
    {
        "archivo": "factura_1003.pdf",
        "numero": "1003",
        "empresa": "Tecnologia Valparaiso SpA",
        "rut": "76.555.444-2",
        "fecha": "25/08/2026",
        "subtotal": "$80.000",
        "iva": "$15.200",
        "total": "$95.200",
    },
]


def crear_factura(datos):
    ruta = f"input/{datos['archivo']}"

    pdf = canvas.Canvas(ruta, pagesize=A4)

    pdf.drawString(100, 780, "FACTURA ELECTRONICA")
    pdf.drawString(100, 740, f"N°: {datos['numero']}")
    pdf.drawString(100, 720, f"Empresa: {datos['empresa']}")
    pdf.drawString(100, 700, f"RUT: {datos['rut']}")
    pdf.drawString(100, 680, f"Fecha: {datos['fecha']}")
    pdf.drawString(100, 640, f"Subtotal: {datos['subtotal']}")
    pdf.drawString(100, 620, f"IVA: {datos['iva']}")
    pdf.drawString(100, 600, f"Total: {datos['total']}")

    pdf.save()


def main():
    for factura in facturas:
        crear_factura(factura)

    print("Facturas de prueba generadas correctamente.")


if __name__ == "__main__":
    main()