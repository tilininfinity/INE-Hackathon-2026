# app/: el prototipo visual

Aquí vive la página del prototipo (micrositio, tablero o visualización). El formato y la herramienta se deciden en `contexto/propuesta_base.md`.

El **diseño** vive aquí y se edita directo; los **datos** los genera Python y nunca entran a git.

| Archivo | Qué es | ¿Se edita a mano? | ¿En git? |
| --- | --- | --- | --- |
| `index.html` | Estructura y textos fijos | Sí | Sí |
| `app.css` | Estilos, con los tokens de `branding/` | Sí | Sí |
| `app.js` | Dibuja todo con los datos | Sí | Sí |
| `../outputs/app/datos.js` | `window.DATOS = {...}`, escrito por `scripts/04_pagina.py` | No | **No** (generado) |

Para cambiar el diseño no hace falta Python: edita `index.html`, `app.css` o `app.js` y recarga. Python solo se corre de nuevo si cambian los datos.

Reglas de la página:

- Cada cifra llega de `datos.js`; ninguna se escribe a mano en el HTML.
- Cada gráfica dice su fuente (Plataforma CCPC, INE) y la elección o año.
- Claridad y precisión antes que efecto visual; accesible (contraste, texto alternativo, `prefers-reduced-motion`).
