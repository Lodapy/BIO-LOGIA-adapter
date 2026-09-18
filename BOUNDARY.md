# BIO-LOGIA — límite de privacidad (public boundary)

Este repositorio **público** contiene únicamente un adaptador mínimo. Toda la
lógica de clientes, formularios, payloads, schemas, sesiones, PDFs y medios
sensibles (incluidos audios) viven en el repositorio **privado** `BIO-LOGIA`,
detrás de acceso autenticado.

## Contrato público

El único punto de integración soportado es `src/client_features_adapter.py`,
un shim delgado que llama a un backend privado con Bearer token y scoping por
cliente/tenant.

Secretos de despliegue requeridos (nunca en el repo):
- `CLIENT_FEATURES_BASE_URL`
- `CLIENT_FEATURES_TOKEN`

El adaptador **falla cerrado** si esas variables no están configuradas.

## Prohibido en este repositorio público

- `src/strateia/intake.py`, `agro_intake.py`, `intake_cargill.py`
- `src/strateia/static/cliente_intake*.html`
- `tests/test_intake_agro.py`
- `bovinoscan-intake/` y cualquier audio (`*.ogg`, `*.opus`, `*.m4a`, `*.mp3`, `*.wav`)
- rutas y schemas específicos de cliente (`/intake`, `/sessions/intake/*`, `/results/intake/*`)
- datos, IDs o payloads de cliente en cualquier archivo
- cualquier `.env` o secreto

El workflow `.github/workflows/public-boundary.yml` hace **fail** si alguno de
esos paths aparece rastreado en el repo.

## Historia

Este repositorio se creó **limpio** (historia nueva). El código real y su
historial permanecen en el repo privado `BIO-LOGIA`. No hubo reescritura de
historial público porque el repo que contenía el material sensible se pasó a
privado en su totalidad (contención completa), en vez de purgar rutas sueltas.
