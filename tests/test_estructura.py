"""Pruebas de la estructura del repo: configuración legible y bitácora con nombres válidos."""

import re
from datetime import date

from participa.config import RAIZ, params

PATRON_CAMBIO = re.compile(r"^C(\d{2})_(\d{2})(\d{2})\.md$")


def test_params_carga_y_trae_la_fuente() -> None:
    p = params()
    assert "ine.mx" in p["fuente"]["url"]
    assert p["elecciones"]["desde"] <= p["elecciones"]["hasta"]


def test_bitacora_sigue_el_formato() -> None:
    # NOTA1: CAMBIOS/ solo existe en la rama tests; en main la prueba no tiene nada que revisar.
    carpeta = RAIZ / "CAMBIOS"
    if not carpeta.exists():
        return
    numeros = []
    for archivo in carpeta.glob("C*.md"):
        coincidencia = PATRON_CAMBIO.match(archivo.name)
        assert coincidencia, f"{archivo.name} no sigue C##_ddmm.md"
        numero, dia, mes = (int(g) for g in coincidencia.groups())
        date(2026, mes, dia)  # falla si la fecha no existe
        numeros.append(numero)
    assert len(numeros) == len(set(numeros)), "Hay números de cambio repetidos"
