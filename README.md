# Hackea la participación: Datos que construyen democracia

Proyecto del equipo para el **Hackathon INE 2026**, convocado por el Instituto Nacional Electoral (DECEyEC).

> **Eje temático:** Storytelling con datos
> **Reto 3:** Comunicación y visualización con impacto público
> **Pregunta guía:** ¿Cómo traducir los datos de participación en mensajes comprensibles para la ciudadanía?

## 🎯 Objetivo

Diseñar materiales visuales y narrativos que expliquen de forma sencilla **por qué es importante participar**, **cuáles son los niveles de participación** y **cómo varían entre grupos o regiones**, usando los datos de la [Plataforma de los Conteos Censales de Participación Ciudadana (CCPC) 2009–2024](https://ine.mx/transparencia/datos-abiertos/visualizacion-datos/conteos-censales-participacion/).

Lo que debemos hacer, según la convocatoria:

1. Definir el **mensaje central** y el **público** al que se dirige la pieza.
2. Diseñar una **narrativa con datos** clara, veraz y atractiva.
3. Desarrollar un **prototipo visual funcional** (micrositio, dashboard o visualización).
4. Elaborar una **propuesta de difusión** para llevar la pieza a su público.

> Priorizar la claridad y la precisión de la información sobre el efecto visual.

## 📦 Entregables

**Fecha límite: 31 de octubre de 2026, 23:59 h.** Se envía todo en un `.zip` con el nombre del equipo y el eje temático.

| Entregable | Formato | Carpeta | Estado |
|---|---|---|---|
| Prototipo visual (infografía, tablero interactivo o carrusel) | PDF / PNG / enlace web | `entregables/prototipo/`, `web/` | ⬜ |
| Guion narrativo (storyline + propuesta de difusión), 3 a 5 cuartillas | PDF | `entregables/guion-narrativo/` | ⬜ |
| Video explicativo / pitch, máx. 3 min | MP4 1080p, enlace (YouTube oculto / Drive) | `entregables/video/` | ⬜ |
| Presentación ejecutiva, máx. 10 diapositivas | PDF / PPTX | `entregables/presentacion/` | ⬜ |
| Código o enlace al repositorio | Este repo | — | ⬜ |
| Carta de cesión de derechos (firmada por todo el equipo) | PDF | **Fuera del repo** | ⬜ |
| Carta declaratoria de decir verdad (firmada por todo el equipo) | PDF | **Fuera del repo** | ⬜ |

> ⚠️ La omisión de cualquier entregable obligatorio es causa de descalificación.

## 🧭 Criterios de evaluación

- **Apego a la temática:** responde al Reto 3 y aprovecha los datos de la Plataforma CCPC.
- **Claridad y solidez:** planteamiento, método y hallazgos claros y bien sustentados.
- **Originalidad y creatividad:** mirada novedosa, producto creativo y útil.
- **Viabilidad institucional:** se puede adaptar o implementar en acciones del INE.
- **Potencial de aplicación:** puede convertirse en un proyecto real dentro del INE.

## 🗂️ Estructura del repositorio

```
.
├── data/
│   ├── raw/            # Descargas originales de la Plataforma CCPC (no se versionan)
│   ├── interim/        # Transformaciones intermedias (no se versionan)
│   ├── processed/      # Datos limpios y ligeros que usa el prototipo
│   └── external/       # Otras fuentes públicas de apoyo (INEGI, etc.)
├── notebooks/          # Exploración y análisis (Jupyter)
├── src/                # Código reutilizable de limpieza y cálculo de indicadores
├── scripts/            # Scripts de descarga / procesamiento de punta a punta
├── web/                # Prototipo visual (micrositio / dashboard)
├── assets/             # Imágenes, íconos y fuentes del diseño
├── docs/               # Documentación del proyecto
│   ├── decisiones/     # Registro de decisiones importantes
│   └── ...
├── entregables/        # Versiones finales de lo que se envía al INE
└── .github/            # Plantillas de issues y pull requests
```

## 🚀 Cómo empezar

```bash
git clone https://github.com/tilininfinity/INE-Hackathon-2026.git
cd INE-Hackathon-2026

# Entorno de análisis (Python 3.11+)
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Coloca las descargas de la Plataforma CCPC en `data/raw/` (ver [`data/README.md`](data/README.md)).

## 👥 Equipo

| Integrante | Rol |
|---|---|
| Hector ([@tilininfinity](https://github.com/tilininfinity)) | Por definir |
| Chamuel | Por definir |
| Claude (asistente de IA) | Apoyo en análisis, código y redacción |

Lee [CONTRIBUTING.md](CONTRIBUTING.md) para saber cómo trabajamos.

## 🔒 Datos y privacidad

- Trabajamos **solo con datos agregados y públicos** de la Plataforma CCPC; nunca con datos personales.
- Las cartas firmadas, credenciales para votar y estados de cuenta **no se suben a este repositorio** (es público).

## ⚖️ Derechos

Conforme a la base Décimo Primera de la convocatoria, los derechos patrimoniales de los trabajos presentados se ceden al INE por 10 años, con fines institucionales y/o educativos. Las personas autoras conservan el reconocimiento de autoría.
