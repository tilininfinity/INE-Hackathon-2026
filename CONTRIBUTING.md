# Cómo contribuir

Somos un equipo pequeño con poco tiempo (entrega: **31 de octubre de 2026**), así que el flujo es ligero pero ordenado.

## 1. Organización del trabajo

- Cada tarea vive en un **issue**. Usa las plantillas (Tarea, Bug, Idea de narrativa).
- Asígnate el issue antes de empezar para que nadie duplique trabajo.
- Usamos etiquetas por área: `datos`, `narrativa`, `diseño`, `web`, `entregable`, `difusión`.

## 2. Ramas

`main` siempre debe tener una versión que funcione. Nadie sube cambios directo a `main`.

Nombra tu rama con el tipo y una descripción corta:

| Prefijo | Para qué | Ejemplo |
|---|---|---|
| `datos/` | Descarga, limpieza, indicadores | `datos/limpieza-ccpc-2024` |
| `viz/` | Gráficas y prototipo visual | `viz/mapa-participacion-estatal` |
| `docs/` | Guion, documentación, textos | `docs/guion-narrativo-v1` |
| `fix/` | Correcciones | `fix/porcentajes-por-edad` |

```bash
git checkout main
git pull
git checkout -b viz/mapa-participacion-estatal
```

## 3. Commits

Mensajes cortos, en español y en imperativo:

```
Agrega gráfica de participación por grupo de edad
Corrige cálculo de abstención en 2018
```

## 4. Pull requests

1. Sube tu rama: `git push -u origin nombre-de-tu-rama`.
2. Abre un PR hacia `main` y llena la plantilla.
3. Pide revisión de al menos **una persona** del equipo.
4. Quien revisa comprueba que los datos citados sean correctos y que el texto sea claro.
5. Cuando esté aprobado, se fusiona con **Squash and merge** y se borra la rama.

## 5. Reglas para datos

- Las descargas originales van en `data/raw/` y **no se suben** (están en `.gitignore`). Documenta en `data/README.md` de dónde salió cada archivo.
- Todo número que aparezca en una visualización o en el guion debe poder rastrearse a un notebook o script.
- Solo datos agregados. **Nunca** datos personales.
- Anota la fuente y el año en cada gráfica.

## 6. Notebooks

- Nómbralos con número e iniciales: `01-exploracion-ccpc-HE.ipynb`.
- Antes de hacer commit, reinicia el kernel y ejecuta todo de principio a fin.
- Si algo del notebook se reutiliza, muévelo a `src/`.

## 7. Decisiones

Cuando tomemos una decisión importante (mensaje central, público objetivo, herramienta del prototipo), regístrala en `docs/decisiones/` con la plantilla que ahí se incluye. Así nadie tiene que preguntar dos veces por qué hicimos algo.

## 8. Archivos que no van en el repo

- Cartas firmadas, credenciales y cualquier documento con datos personales.
- Videos y archivos pesados: súbelos a Drive o YouTube (modo oculto) y pon el enlace en `entregables/video/README.md`.
- Archivos `.env` o contraseñas.
