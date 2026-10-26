# INE Hackathon 2026 · Reto 3 — contexto para Claude Code

Proyecto de Samuel (alias **chamuel**) y Héctor (alias **Tilin**) para el Hackathon INE 2026, "Hackea la participación: Datos que construyen democracia" (INE, DECEyEC). Responde siempre en español.

## Qué construimos

Una pieza de **storytelling con datos** sobre la participación ciudadana en México, hecha con la Plataforma de los Conteos Censales de Participación Ciudadana (CCPC) 2009–2024. Eje elegido: **Reto 3, Comunicación y visualización con impacto público**.

Pregunta guía: ¿cómo traducir los datos de participación en mensajes comprensibles para la ciudadanía? La pieza explica de forma sencilla por qué es importante participar, cuáles son los niveles de participación y cómo varían entre grupos o regiones. Texto completo en `contexto/propuesta_base.md`.

Lo que pide la convocatoria para este reto:
1. Definir el **mensaje central** y el **público** de la pieza.
2. Diseñar una **narrativa con datos** clara, veraz y atractiva.
3. Desarrollar un **prototipo visual funcional** (micrositio, dashboard o visualización).
4. Elaborar una **propuesta de difusión** para llevar la pieza a su público.

Entregables (correo a grecia.castro@ine.mx y cirse.rodriguez@ine.mx, un `.zip` con nombre del equipo y eje, **sábado 31 de octubre de 2026, 23:59**):
- **Del reto:** prototipo visual (PDF, PNG o enlace web interactivo); guion narrativo de 3 a 5 cuartillas en PDF (storyline y propuesta de difusión: canales, formato, público); video explicativo o pitch de máximo 3 minutos, MP4 1080p, alojado con permiso de lectura.
- **Generales:** presentación ejecutiva (máximo 10 diapositivas), código o enlace al repositorio, carta de cesión de derechos y carta declaratoria de decir verdad firmadas por todo el equipo.
- La omisión de cualquier entregable obligatorio descalifica.

Criterios de evaluación (comité de 5 especialistas): apego a la temática y uso de la Plataforma CCPC; claridad y solidez; originalidad y creatividad; viabilidad para el aprovechamiento institucional; potencial de aplicación en proyectos reales del INE.

## Decisiones tomadas

- Eje: Reto 3 (storytelling con datos).
- Estructura del repo, flujo de trabajo y ramas `tests`/`main` siguen el modelo de Ojo de Águila (proyecto anterior del equipo).
- Pendiente: nombre del proyecto, mensaje central, público objetivo, formato y herramienta del prototipo.

## Reglas no negociables

1. **Datos**: solo agregados y públicos de la Plataforma CCPC. Nunca datos personales. `data/` y `outputs/` jamás entran a git.
2. **Documentos personales**: cartas firmadas, credenciales para votar y estados de cuenta nunca entran al repo (es público).
3. **Veracidad**: cada cifra que ve la ciudadanía sale del código, con su definición en `contexto/propuesta_base.md` y su parámetro en `config/params.yaml`. Sin números escritos a mano en la página ni en el guion.
4. **No inventes campos**: antes de usar una columna de la plataforma, revísala en los archivos descargados. Si algo difiere de lo esperado, avísalo y anótalo.
5. **Honestidad**: separar correlación de causalidad; marcar supuestos; claridad y precisión por encima del efecto visual (lo pide la convocatoria).
6. **Neutralidad**: la pieza promueve la participación, nunca a un partido, candidatura o postura política.

## Entorno

- Windows + PowerShell, Python 3.13, `venv`, `requirements.txt` con versiones fijas, VS Code + Jupyter.
- Rutas con `pathlib`; nada de rutas absolutas ni separadores fijos. Cuidado con OneDrive y rutas con acentos.
- Activar el entorno: `.venv\Scripts\Activate.ps1` (si falla: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`).

## Cómo trabajar

- El código reutilizable va en `src/participa/`, por capas `ingesta → datos → indicadores → salidas`; los notebooks son solo exploración y llaman a `src/`.
- La página se diseña en `app/` (HTML, CSS y JS editables a mano y versionados); Python solo escribe sus datos en `outputs/app/` (fuera de git). Contrato en `app/README.md`.
- Funciones pequeñas con docstring en español, tipadas, sin efectos ocultos. Identificadores en español sin acentos.
- Cada script nuevo trae instrucciones para probarlo; agrega pruebas en `tests/` con fixtures sintéticas.
- Antes de cambios grandes, propone el plan y los archivos que tocarás.
- Commits pequeños y descriptivos (`área: qué cambió`); nunca subir datos ni salidas.
- Todos siguen `contexto/flujo_trabajo.md`: tamaño de la tarea, 5 fases (entender, planear, criterios de calidad, ejecutar, revisar), día a día y trabajo en paralelo.
- Comentarios con la simbología de `contexto/flujo_trabajo.md`, sección 7: `NOTAn`, `OBSn`, `REFn`, `IMPORn`, `TODOn`, `FIXn`, `HACKn`, `PERFn`, `DEPRECn`, numerados por archivo. Todo `TODOn` y `HACKn` se anota también en **Por hacer** de la bitácora.
- Bitácora `CAMBIOS/` (solo en la rama `tests`): un archivo por día, `C##_ddmm.md` (reglas en `CAMBIOS/README.md`). Al terminar un trabajo, actualiza el archivo del día con el alias de quien lo pidió y "(con Claude Code)".
- Ramas: `tests` = TESTS (trabajo diario, incluye `CAMBIOS/`); `main` = FINAL (solo lo confirmado, sin `CAMBIOS/`). A `main` se llega solo por PR desde una rama `promocion/ddmm` (`contexto/flujo_trabajo.md`, sección 5); nunca commits directos ni PR directo `tests → main`.
- `git pull` antes de empezar.

## Estado actual (actualizar al avanzar)

- [x] Convocatoria analizada (26 oct).
- [x] Repo y estructura definidos (26 oct, ver `README.md`).
- [ ] Entorno instalado y `python -m pytest` pasa en las laptops del equipo.
- [ ] Descarga e inventario de la Plataforma CCPC.
- [ ] Mensaje central y público objetivo.
- [ ] Hallazgos y storyline.
- [ ] Prototipo visual.
- [ ] Guion narrativo y propuesta de difusión.
- [ ] Video, presentación, cartas y envío.

## Documentos (léelos solo cuando la tarea lo pida)

- `contexto/propuesta_base.md`: reto, mensaje, público, indicadores y cómo se cubre cada criterio de evaluación.
- `contexto/plan_trabajo.md`: calendario día a día hasta el 31 de octubre y checklist de envío.
- `contexto/flujo_trabajo.md`: cómo trabajamos en equipo: fases, día a día, ramas y promoción a `main`, commits y simbología de comentarios.
- `contexto/guion_narrativo.md`: borrador del guion narrativo (entregable) y de la propuesta de difusión.
- `contexto/uso_ia.md`: uso de IA generativa (qué hizo Claude Code, qué decidió el equipo y cómo se verificó).
- `app/README.md`: contrato entre la página y sus datos.
- `branding/README.md`: identidad (nombre, paleta, tipografía).
- `CAMBIOS/` (rama `tests`): bitácora diaria; lee el último archivo para saber qué se hizo y qué quedó pendiente.
