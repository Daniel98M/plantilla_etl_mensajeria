# 🌐 Data Sources

| Fuente                 | Descripción                            | Formato     | Actualización | Origen / API       |
|------------------------|----------------------------------------|-------------|----------------|---------------------|
| CRM_Clientes           | Información personal y de contacto     | CSV         | Mensual        | Base interna (BI)   |
| Logs_App               | Eventos de navegación y uso de app     | Parquet     | Diario         | Google BigQuery     |
| Encuestas_NPS          | Resultados de encuestas NPS            | Excel       | Trimestral     | SharePoint externo  |

### Notas:
- La tabla `Logs_App` requiere un proceso de agregación por cliente antes de ser usada.
- Las fechas en `Encuestas_NPS` pueden estar en formato DD/MM/YY, revisar antes de usar.
