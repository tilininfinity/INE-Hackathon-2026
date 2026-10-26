"""Rutas del proyecto y parámetros, resueltos con pathlib desde el paquete."""

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

# src/participa/config.py → parents[2] es la raíz del repo (instalación editable)
RAIZ: Path = Path(__file__).resolve().parents[2]

DIR_DATOS: Path = RAIZ / "data"
DIR_RAW: Path = DIR_DATOS / "raw"
DIR_PROCESADO: Path = DIR_DATOS / "processed"
DIR_LOGS: Path = RAIZ / "logs"
DIR_SALIDAS: Path = RAIZ / "outputs"
ARCHIVO_PARAMS: Path = RAIZ / "config" / "params.yaml"


@lru_cache(maxsize=1)
def params() -> dict[str, Any]:
    """Parámetros del proyecto (config/params.yaml), leídos una sola vez."""
    return yaml.safe_load(ARCHIVO_PARAMS.read_text(encoding="utf-8"))
