# BIO-LOGIA (adapter público)

Capa pública mínima del sistema BIO-LOGIA. **No contiene lógica ni datos de
clientes.** Solo expone un adaptador que integra contra un backend privado
autenticado.

Ver [`BOUNDARY.md`](BOUNDARY.md) para la política de aislamiento.

## Uso

```python
from client_features_adapter import ClientFeaturesClient

client = ClientFeaturesClient()  # lee CLIENT_FEATURES_BASE_URL / _TOKEN del entorno
result = client.submit("cargill", {"campo": "valor"})
```

Requiere las variables de entorno `CLIENT_FEATURES_BASE_URL` y
`CLIENT_FEATURES_TOKEN`. Sin ellas, el cliente falla cerrado.

## Licencia

Software propietario. © 2026 Lodapy. Todos los derechos reservados. No se
concede licencia de uso, copia, modificación ni distribución sin autorización
escrita del titular.
