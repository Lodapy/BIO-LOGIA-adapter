# Política de seguridad

## Reportar una vulnerabilidad

**No abras un issue público** para reportar vulnerabilidades.

Usá el reporte privado de GitHub: pestaña **Security → Report a vulnerability**
(Private Vulnerability Reporting) de este repositorio. Recibirás acuse dentro de
un plazo razonable y coordinaremos la divulgación.

## Alcance

Este repositorio es un **adaptador público mínimo**. La lógica de clientes, los
datos, formularios, sesiones y medios sensibles viven en un repositorio privado,
detrás de acceso autenticado. Ver [`BOUNDARY.md`](BOUNDARY.md).

## Datos de cliente

Este repositorio **no debe contener** datos de cliente, credenciales, IPs
internas ni rutas de intake. El workflow `.github/workflows/public-boundary.yml`
falla si aparece un path sensible. Si detectás material sensible que se haya
filtrado, reportalo por el canal privado de arriba **antes** de abrir un PR.

## Secretos

Nunca incluyas secretos en el código ni en el historial. La integración usa
`CLIENT_FEATURES_BASE_URL` y `CLIENT_FEATURES_TOKEN` provistos por el entorno de
despliegue. Si un secreto se expone, rotalo de inmediato y avisá por el canal
privado.
