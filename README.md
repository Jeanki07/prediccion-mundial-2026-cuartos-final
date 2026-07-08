# Modelo predictivo para cuartos de final del Mundial 2026

Repositorio académico para la **predicción de semifinalistas del Mundial 2026 a partir de los cruces oficiales de cuartos de final**.

El proyecto integra resultados actualizados, ranking FIFA, ranking Elo, forma reciente, contexto competitivo, modelos de regresión, distribución de Poisson, análisis de tarjetas y visualizaciones para sustentar la predicción de los equipos que avanzan a semifinales.

---

## Integrantes del grupo

- Jean Frank Bustamante Vela
- Miguel Angel Marreros Cortegana
- Valentin Fernandez Campos
- Frank Salon Trigoso
- Maria Carmen Tuesta Chuquizuta

---

## Enlace del repositorio

```text
https://github.com/Jeanki07/prediccion-mundial-2026-cuartos-final
```

---

## Objetivo del proyecto

Construir un modelo predictivo para los partidos de **cuartos de final del Mundial 2026**, con el fin de estimar:

- Marcadores probables en 90 minutos.
- Probabilidades de victoria, empate y clasificación.
- Equipos clasificados a semifinales.
- Posibles tarjetas por partido.
- Modelo con mejor desempeño según métricas.
- Influencia del ranking FIFA, ranking Elo y forma reciente.

---

## Cruces de cuartos de final analizados

```text
France vs Morocco
Spain vs Belgium
Norway vs England
Argentina vs Switzerland
```

Estos cruces se trabajan como partidos reales de cuartos de final; por tanto, el repositorio ya no se centra en predecir quién llega a cuartos, sino en **predecir quién avanza a semifinales**.

---

## Metodología general

El flujo del proyecto es:

```text
1. Actualización de resultados oficiales.
2. Construcción de fixtures reales de cuartos.
3. Generación de variables de contexto.
4. Reentrenamiento de modelos con la data actualizada.
5. Comparación de modelos mediante métricas.
6. Selección del mejor modelo base.
7. Cálculo de goles esperados.
8. Estimación de marcadores con Poisson.
9. Predicción de clasificados a semifinales.
10. Análisis de tarjetas y Fair Play.
11. Visualización integral de resultados.
```

---

## Variables consideradas

El modelo no se basa solo en el nombre de los equipos. Utiliza variables cuantitativas y de contexto:

```text
- Goles recientes a favor.
- Goles recientes en contra.
- Puntos obtenidos en los últimos partidos.
- Cantidad de partidos recientes usados.
- Ranking FIFA.
- Ranking Elo.
- Diferencia FIFA entre equipos.
- Diferencia Elo entre equipos.
- Historial directo.
- Ventaja contextual.
- Rendimiento ofensivo.
- Rendimiento defensivo.
- Fair Play.
- Tarjetas amarillas y rojas.
```

---

## Modelos evaluados

Se comparan cinco modelos:

```text
1. Regresión Lineal
2. Ridge Regression
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. Poisson Regressor
```

La competencia de modelos se evalúa con:

```text
- MAE
- RMSE
- R²
- Score compuesto
```

El objetivo no es elegir un modelo por intuición, sino por desempeño medible.

---

## Interpretación del modelo Ridge

El modelo Ridge se incluye como lectura complementaria porque tiende a ser más conservador en los marcadores.  
En partidos parejos puede estimar empates en los 90 minutos. En ese caso, el clasificado no se decide arbitrariamente: se revisa la probabilidad estimada, el ranking Elo, el ranking FIFA y la forma reciente.

Esto permite diferenciar entre:

```text
- Resultado probable en 90 minutos.
- Equipo con mayor probabilidad de avanzar.
```

---

## Estructura principal del repositorio

```text
.
├── README.md
├── requirements.txt
├── 00_actualizar_datos_oficiales.py
├── 02_reentrenar_modelos_actualizados.py
├── 10_ver_metricas_modelos.py
├── 12_actualizar_fixtures_modelo_cuartos.py
├── 13_predecir_semifinales.py
├── 14_panel_integral_cuartos.py
├── 15_ver_prediccion_ridge_cuartos.py
├── data
│   ├── results.csv
│   ├── data_modelo.csv
│   ├── fixtures_cuartos.csv
│   ├── fixtures_cuartos_modelo.csv
│   ├── fair_play.csv
│   ├── fifa_ranking.csv
│   ├── elo_ranking.csv
│   └── tarjetas_octavos_reales.csv
└── outputs
    ├── competencia_modelos.csv
    ├── resumen_metricas_modelos.csv
    ├── mejor_modelo.txt
    ├── prediccion_cuartos_a_semifinales.csv
    ├── top10_marcadores_cuartos.csv
    ├── prediccion_tarjetas_cuartos.csv
    ├── clasificados_semifinales.csv
    ├── analisis_contexto_cuartos.csv
    ├── prediccion_ridge_cuartos.csv
    ├── panel_competencia_modelos.png
    ├── panel_metricas_modelos.png
    ├── panel_cuartos_marcadores_tarjetas.png
    ├── panel_integral_cuartos.png
    └── panel_ridge_cuartos.png
```

---

## Scripts principales

### 00_actualizar_datos_oficiales.py

Actualiza los resultados oficiales recientes y deja preparada la base para trabajar con los partidos reales de cuartos.

---

### 12_actualizar_fixtures_modelo_cuartos.py

Construye las variables necesarias para que los partidos de cuartos puedan ser evaluados por los modelos.

Genera:

```text
data/fixtures_cuartos_modelo.csv
data/results_actualizado_cuartos.csv
data/fixtures_modelo_actualizado_cuartos.csv
```

---

### 02_reentrenar_modelos_actualizados.py

Reentrena los cinco modelos usando la data general actualizada.

Genera:

```text
outputs/competencia_modelos.csv
outputs/resumen_metricas_modelos.csv
outputs/mejor_modelo.txt
outputs/panel_competencia_modelos.png
outputs/panel_metricas_modelos.png
outputs/modelo_home.pkl
outputs/modelo_away.pkl
```

Este paso permite que las predicciones incorporen los resultados más recientes.

---

### 13_predecir_semifinales.py

Predice los partidos de cuartos de final y estima qué equipos avanzan a semifinales.

Genera:

```text
outputs/prediccion_cuartos_a_semifinales.csv
outputs/top10_marcadores_cuartos.csv
outputs/prediccion_tarjetas_cuartos.csv
outputs/clasificados_semifinales.csv
outputs/panel_cuartos_marcadores_tarjetas.png
```

---

### 10_ver_metricas_modelos.py

Muestra las métricas de los modelos guardadas previamente.

Genera:

```text
outputs/resumen_metricas_modelos.csv
outputs/panel_metricas_modelos.png
```

---

### 14_panel_integral_cuartos.py

Genera una visualización general con la información más importante del proyecto:

```text
- Cruce de cuartos.
- Ranking FIFA.
- Ranking Elo.
- Diferencias entre equipos.
- Lambdas finales.
- Probabilidades.
- Marcador estimado.
- Clasificado proyectado.
- Tarjetas esperadas.
- Riesgo disciplinario.
- Mejor modelo usado.
```

Salida principal:

```text
outputs/panel_integral_cuartos.png
```

---

### 15_ver_prediccion_ridge_cuartos.py

Muestra una lectura específica del modelo Ridge para comparar su comportamiento frente al modelo principal.

Genera:

```text
outputs/prediccion_ridge_cuartos.csv
outputs/panel_ridge_cuartos.png
```

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Jeanki07/prediccion-mundial-2026-cuartos-final.git
cd prediccion-mundial-2026-cuartos-final
```

---

### 2. Crear entorno virtual

En Linux o macOS:

```bash
python -m venv venv
source venv/bin/activate
```

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución completa recomendada

Para evaluar el proyecto de manera completa, ejecutar:

```bash
python 00_actualizar_datos_oficiales.py
python 12_actualizar_fixtures_modelo_cuartos.py
python 02_reentrenar_modelos_actualizados.py
python 13_predecir_semifinales.py
python 10_ver_metricas_modelos.py
python 14_panel_integral_cuartos.py
python 15_ver_prediccion_ridge_cuartos.py
```

---

## Ejecución rápida

Si el profesor desea revisar la entrega sin reentrenar los modelos:

```bash
python 00_actualizar_datos_oficiales.py
python 12_actualizar_fixtures_modelo_cuartos.py
python 13_predecir_semifinales.py
python 10_ver_metricas_modelos.py
python 14_panel_integral_cuartos.py
```

El reentrenamiento puede tardar más porque vuelve a ajustar los cinco modelos.

---

## Archivos de salida más importantes

### Predicción principal de cuartos a semifinales

```text
outputs/prediccion_cuartos_a_semifinales.csv
```

Contiene:

```text
- Equipo local.
- Equipo visitante.
- Lambdas estimadas.
- Marcador probable.
- Probabilidad de victoria local.
- Probabilidad de empate.
- Probabilidad de victoria visitante.
- Clasificado estimado.
```

---

### Clasificados a semifinales

```text
outputs/clasificados_semifinales.csv
```

Contiene los equipos que el modelo proyecta como semifinalistas.

---

### Top 10 marcadores por partido

```text
outputs/top10_marcadores_cuartos.csv
```

Muestra los diez marcadores más probables para cada cruce.

---

### Predicción de tarjetas

```text
outputs/prediccion_tarjetas_cuartos.csv
```

Incluye:

```text
- Tarjetas esperadas por equipo.
- Total esperado de tarjetas.
- Riesgo disciplinario.
- Contexto del partido.
```

---

### Competencia de modelos

```text
outputs/competencia_modelos.csv
outputs/resumen_metricas_modelos.csv
outputs/panel_competencia_modelos.png
outputs/panel_metricas_modelos.png
```

Permite identificar cuál modelo tuvo mejor desempeño.

---

### Panel integral

```text
outputs/panel_integral_cuartos.png
```

Es la visualización principal de la entrega porque resume modelo, contexto, ranking, probabilidades y tarjetas.

---

## Comandos útiles de revisión

### Ver predicción principal

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/prediccion_cuartos_a_semifinales.csv'); print(df.to_string(index=False))"
```

### Ver clasificados a semifinales

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/clasificados_semifinales.csv'); print(df.to_string(index=False))"
```

### Ver competencia de modelos

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/competencia_modelos.csv'); print(df.to_string(index=False))"
```

### Ver lectura Ridge

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/prediccion_ridge_cuartos.csv'); print(df.to_string(index=False))"
```

### Abrir panel integral en Linux

```bash
xdg-open outputs/panel_integral_cuartos.png
```

### Abrir panel de competencia de modelos

```bash
xdg-open outputs/panel_competencia_modelos.png
```

---

## Enfoque de evaluación

Este repositorio debe evaluarse como un sistema predictivo aplicado a una fase específica del torneo:

```text
Cuartos de final reales → predicción de semifinalistas
```

La fortaleza del trabajo está en que combina:

```text
- Resultados actualizados.
- Variables deportivas de contexto.
- Ranking FIFA.
- Ranking Elo.
- Forma reciente.
- Competencia de modelos.
- Métricas comparativas.
- Predicción probabilística de marcadores.
- Análisis de tarjetas.
- Visualización integral.
```

---

## Nota final

El modelo no pretende asegurar resultados exactos, sino construir una estimación fundamentada con datos.  
En fútbol existe incertidumbre, por lo que la predicción debe interpretarse como una probabilidad basada en evidencia y no como una certeza absoluta.
