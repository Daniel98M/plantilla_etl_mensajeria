# 🧪 Experimentation Log

Registro cronológico de los experimentos realizados durante el desarrollo del modelo.

| Fecha       | Descripción breve                  | Cambios implementados                          | Métricas clave              | Resultado / Conclusión                |
|-------------|------------------------------------|------------------------------------------------|-----------------------------|---------------------------------------|
| 2025-05-15  | Baseline con RandomForest          | Default hyperparams, sin balanceo de clases    | Acc: 0.82, F1: 0.75         | Buen inicio, bajo recall             |
| 2025-05-17  | Añadido balanceo con SMOTE         | Aplicado SMOTE sobre clase minoritaria         | Acc: 0.80, F1: 0.80         | Mejor F1, ligeramente menos precisión|
| 2025-05-20  | LightGBM con tuning de parámetros  | Grid search con early stopping                 | Acc: 0.87, F1: 0.81         | Mejor modelo hasta ahora             |

### Notas:
- SMOTE mejoró el recall sin dañar mucho el accuracy.
- LightGBM permite mayor interpretabilidad con SHAP.
