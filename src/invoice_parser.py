import re


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


def factura_valida(datos):
    campos_obligatorios = [
        datos["numero"],
        datos["empresa"],
        datos["rut"],
        datos["fecha"],
        datos["total"],
    ]

    return all(campo is not None for campo in campos_obligatorios)