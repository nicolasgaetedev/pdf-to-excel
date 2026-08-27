import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from invoice_parser import (
    convertir_monto,
    extraer_datos_factura,
    factura_valida,
    obtener_campos_faltantes,
)


def test_convertir_monto():
    assert convertir_monto("119.000") == 119000


def test_convertir_monto_none():
    assert convertir_monto(None) is None


def test_extraer_datos_factura():
    texto = """
    N°: 1001
    Empresa: Comercial Andes SpA
    RUT: 76.123.456-7
    Fecha: 27/08/2026
    Subtotal: $100.000
    IVA: $19.000
    Total: $119.000
    """

    datos = extraer_datos_factura(texto)

    assert datos["numero"] == "1001"
    assert datos["empresa"] == "Comercial Andes SpA"
    assert datos["rut"] == "76.123.456-7"
    assert datos["fecha"] == "27/08/2026"
    assert datos["subtotal"] == 100000
    assert datos["iva"] == 19000
    assert datos["total"] == 119000


def test_factura_valida():
    datos = {
        "numero": "1001",
        "empresa": "Comercial Andes SpA",
        "rut": "76.123.456-7",
        "fecha": "27/08/2026",
        "subtotal": 100000,
        "iva": 19000,
        "total": 119000,
    }

    assert factura_valida(datos) is True


def test_factura_invalida():
    datos = {
        "numero": "1001",
        "empresa": None,
        "rut": None,
        "fecha": "27/08/2026",
        "subtotal": 100000,
        "iva": 19000,
        "total": None,
    }

    assert factura_valida(datos) is False

    campos_faltantes = obtener_campos_faltantes(datos)

    assert "Empresa" in campos_faltantes
    assert "RUT" in campos_faltantes
    assert "Total" in campos_faltantes