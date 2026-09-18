# Contribuir a BIO-LOGIA (adapter público)

Gracias por tu interés. Este repositorio es una **capa pública mínima**: solo el
adaptador y su documentación. Toda la lógica y los datos de clientes viven en el
repositorio privado.

## Regla número uno: el límite de privacidad

Ver [`BOUNDARY.md`](BOUNDARY.md). **Nunca** agregues a este repo:

- código, formularios, schemas o rutas específicas de cliente (`/intake`,
  `/sessions/intake/*`, `/results/intake/*`, `cliente_intake*`, `intake_cargill`,
  `agro_intake`, etc.);
- datos, IDs o payloads de cliente;
- audios u otros medios (`*.ogg`, `*.opus`, `*.m4a`, `*.mp3`, `*.wav`);
- `.env`, tokens o cualquier secreto;
- IPs o hostnames internos.

El workflow `public-boundary.yml` hace **fail** si alguno de esos paths aparece.
Si tu cambio los necesita, va al repositorio privado, no acá.

## Flujo de trabajo

1. Abrí un issue describiendo el cambio antes de codificar.
2. Ramá desde `main` con `feature/<tema>` o `fix/<tema>`.
3. Mantené el adaptador delgado: sin persistencia, sin lógica de negocio, sin
   estado de cliente. Solo integración autenticada contra el backend privado.
4. Verificá localmente que el CI de frontera pasa.
5. Abrí el PR usando la plantilla; no lo fusiones vos.

## Estilo

- Python: mantené el módulo autocontenido y con dependencias mínimas (`httpx`).
- Fail-closed: si falta configuración, el cliente debe fallar de forma explícita.
