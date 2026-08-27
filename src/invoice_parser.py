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


def obtener_campos_faltantes(datos):
    campos_obligatorios = {
        "N° Factura": datos["numero"],
        "Empresa": datos["empresa"],
        "RUT": datos["rut"],
        "Fecha": datos["fecha"],
        "Total": datos["total"],
    }

    return [
        nombre
        for nombre, valor in campos_obligatorios.items()
        if valor is None
    ]


def factura_valida(datos):
    return len(obtener_campos_faltantes(datos)) == 0