# INE Hackathon 2026 · Reto 3

Storytelling con los datos de la [Plataforma de los Conteos Censales de Participación Ciudadana (CCPC) 2009–2024](https://ine.mx/transparencia/datos-abiertos/visualizacion-datos/conteos-censales-participacion/) para el **Hackathon INE 2026, "Hackea la participación: Datos que construyen democracia"**. Eje: **Comunicación y visualización con impacto público**.

**Pregunta guía:** ¿cómo traducir los datos de participación en mensajes comprensibles para la ciudadanía?

Repositorio público: aquí se versiona código, documentación y diseño, **nunca datos descargados, salidas generadas ni documentos personales** de la entrega. Contexto completo en [`CLAUDE.md`](CLAUDE.md) y [`contexto/`](contexto/).

## Instalación (Windows, PowerShell, Python 3.13)

Desde la raíz del repo:

```powershell
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1          # si falla: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
python -m pip install -r requirements.txt
nbstripout --install                # una vez por clon: guarda los notebooks sin salidas
```

`requirements.txt` instala también el paquete `participa` en modo editable, así que scripts y notebooks hacen `from participa...` sin tocar `sys.path`.

Verificación: `python -m pytest` debe pasar completo.

## Del dato a la historia

Los scripts se corren en orden; todos son incrementales (lo ya hecho se salta). **Aún no existen:** la tabla es el plan y se actualiza conforme se construyen.

| Paso | Comando | Red | Qué hace |
| --- | --- | --- | --- |
| 1 | `python scripts/01_descarga.py` | Sí | Descarga de la Plataforma CCPC → `data/raw/` |
| 2 | `python scripts/02_procesar.py` | No | Crudo → tablas limpias en `data/processed/` |
| 3 | `python scripts/03_indicadores.py` | No | Participación por elección, grupo y región → `outputs/indicadores/` |
| 4 | `python scripts/04_pagina.py` | No | Datos del prototipo → `outputs/app/datos.js`; la página es `app/index.html` |
| 5 | `python scripts/05_entrega.py` | No | **Entrega**: prototipo autocontenido y exportes PNG/PDF → `outputs/entrega/` |

Los análisis y las pruebas de hallazgos viven en notebooks numerados (`notebooks/NN_tema.ipynb`), que solo llaman a `src/participa`.

## Entrega

Fecha límite: **sábado 31 de octubre de 2026, 23:59 h**, por correo, en un `.zip` con el nombre del equipo y el eje temático (convocatoria, bases Sexta y Séptima). Faltar cualquier entregable obligatorio descalifica.

| Qué | Dónde |
| --- | --- |
| Prototipo visual (infografía, tablero interactivo o carrusel; PDF, PNG o enlace web) | `app/` → `outputs/entrega/` |
| Guion narrativo, 3 a 5 cuartillas, PDF (storyline y propuesta de difusión) | [`contexto/guion_narrativo.md`](contexto/guion_narrativo.md) |
| Video explicativo o pitch, máximo 3 min, MP4 1080p, alojado con permiso de lectura | Se arma fuera del repo; el enlace va en el guion |
| Presentación ejecutiva, máximo 10 diapositivas | Fuera del repo |
| Código o enlace al repositorio | Este repo |
| Carta de cesión de derechos y carta declaratoria de decir verdad, firmadas por todo el equipo | **Nunca en el repo** |

## Créditos, terceros y uso de IA

- **Datos:** Instituto Nacional Electoral, Plataforma CCPC 2009–2024 (datos abiertos y agregados). No se usan datos personales.
- **IA generativa** (detalle en [`contexto/uso_ia.md`](contexto/uso_ia.md)): usamos Claude Code (Anthropic) como asistente de programación y redacción. El mensaje, el público, la interpretación y todo lo que se entrega lo decide el equipo; cada número sale del código.
- **Software libre:** las librerías de `requirements.txt`.
- **Derechos:** por la base Décimo Primera, los derechos patrimoniales de los trabajos se ceden al INE por 10 años con fines institucionales y/o educativos; el equipo conserva la autoría.

## Equipo y forma de trabajo

Samuel (**chamuel**) y Héctor (**Tilin**), con apoyo de Claude Code. Todos seguimos [`contexto/flujo_trabajo.md`](contexto/flujo_trabajo.md): tamaño de la tarea, 5 fases, día a día, ramas, commits y simbología de comentarios (`NOTAn`, `OBSn`, `REFn`, `IMPORn`, `TODOn`, `FIXn`, `HACKn`, `PERFn`, `DEPRECn`).

Lo que hace cada quien se documenta en la bitácora `CAMBIOS/` (solo en la rama `tests`), un archivo por día: `C##_ddmm.md`.

## Ramas: TESTS y FINAL

| Rama | Papel | Cómo se actualiza |
| --- | --- | --- |
| `tests` | **TESTS**: trabajo diario, incluye la bitácora `CAMBIOS/` | Commits directos o PR desde ramas de trabajo (`chamuel/<tema>`, `tilin/<tema>`) |
| `main` | **FINAL**: solo cambios confirmados, sin `CAMBIOS/` | Únicamente por PR desde una rama `promocion/ddmm` (ver `contexto/flujo_trabajo.md`, sección 5) |

Si algo en `tests` deja de funcionar, `main` sigue intacto y se puede volver a él (`git switch main`). Se trabaja siempre en `tests`:

```powershell
git switch tests
git pull                            # antes de empezar, para traer lo último
```

## Estructura

```
INE-Hackathon-2026/
├── CLAUDE.md                 # contexto y reglas para Claude Code
├── CAMBIOS/                  # bitácora del equipo, C##_ddmm.md (solo en la rama tests)
├── app/                      # el prototipo: HTML, CSS y JS editables; Python solo escribe sus datos (ver app/README.md)
├── branding/                 # identidad: nombre, paleta, tipografía, logos (ver branding/README.md)
├── auditoria/                # revisiones del proyecto y lo que se corrigió
├── .github/workflows/        # guardia: un PR a main no puede traer CAMBIOS/
├── README.md
├── pyproject.toml            # metadatos del paquete `participa` (sin dependencias)
├── requirements.txt          # dependencias con versión fija + `-e .`
├── .gitignore                # data/, outputs/, formatos de datos, video y cartas firmadas
├── .gitattributes            # finales de línea y filtro nbstripout
├── config/
│   └── params.yaml           # TODOS los parámetros (nada de números mágicos)
├── contexto/                 # contexto del proyecto (lo lee Claude Code y el equipo)
│   ├── propuesta_base.md     # qué y por qué: reto, mensaje, público, indicadores, criterios
│   ├── plan_trabajo.md       # calendario hasta el 31 oct y checklist de envío
│   ├── flujo_trabajo.md      # cómo trabajamos: fases, ramas, commits, simbología
│   ├── guion_narrativo.md    # borrador del guion (entregable) y propuesta de difusión
│   └── uso_ia.md             # uso de IA generativa: qué hizo, qué decidió el equipo y cómo se verificó
├── src/participa/            # el motor: todo el código reutilizable
│   ├── ingesta/              # capa 1 · descarga de la Plataforma CCPC
│   ├── datos/                # capa 2 · crudo → tablas; único punto de lectura de data/
│   ├── indicadores/          # capa 3 · participación por elección, grupo y región
│   └── salidas/              # capa 4 · figuras y datos de la página
├── scripts/                  # puntos de entrada numerados (tabla de arriba)
├── notebooks/                # exploración numerada (NN_tema.ipynb); solo llaman a src/participa
├── tests/
│   └── fixtures/             # datos SINTÉTICOS hechos a mano, nunca descargas reales
│
│   — solo en local, fuera de git —
├── data/
│   ├── raw/                  # archivos tal como se descargan de la plataforma
│   └── processed/            # tablas normalizadas
└── outputs/                  # todo lo generado: indicadores, figuras, app/datos.js y entrega/
```

## Reglas de la estructura

1. **Las capas van en un solo sentido:** `ingesta → datos → indicadores → salidas`. Una capa nunca importa a una posterior.
2. **Un solo acceso a la red y a los datos:** solo `participa.ingesta` descarga y solo `participa.datos` lee `data/`. Scripts y notebooks piden tablas a `participa.datos`.
3. **Nada fijo en el código:** elecciones, regiones, grupos y umbrales salen de `config/params.yaml`.
4. **Scripts y notebooks son delgados:** orquestan y exploran; la lógica que sirva dos veces se mueve a `src/participa/`.
5. **Pruebas sin datos reales:** `tests/` usa fixtures sintéticas, así cualquiera las corre sin descargar nada.
6. **Lo generado no se versiona:** va a `outputs/`. Un resultado se comparte a propósito, nunca por accidente.
7. **La página se diseña a mano y se alimenta de datos:** `app/` es HTML, CSS y JS editables; `scripts/04_pagina.py` solo escribe `outputs/app/datos.js`.
8. **Cada cifra que ve la ciudadanía tiene definición y fuente:** la definición en `contexto/propuesta_base.md`, el parámetro en `config/params.yaml` y la prueba en `tests/`. Claridad y precisión por encima del efecto visual.
