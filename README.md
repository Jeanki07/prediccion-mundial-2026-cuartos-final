# Modelo predictivo para cuartos de final del Mundial 2026

Este repositorio contiene la entrega correspondiente al **modelo predictivo para los cuartos de final del Mundial 2026**.

El objetivo principal es simular los partidos de cuartos de final, estimar marcadores probables, calcular probabilidades de clasificación a semifinales y analizar el riesgo disciplinario mediante datos de Fair Play y tarjetas.

---

## Integrantes del grupo

- Jean Frank Bustamante Vela
- Miguel Angel Marreros Cortegana
- Valentin Fernandez Campos
- Frank Salon Trigoso
- Maria Carmen Tuesta Chuquizuta

---

## Entrega

**Modelo predictivo para los cuartos de final del Mundial 2026.**

Esta entrega se enfoca en la fase de **cuartos de final**, es decir, en la predicción de los partidos que definen qué selecciones clasifican a **semifinales**.

---

## Enlaces individuales de GitHub

- Jean Frank Bustamante Vela: https://github.com/Jeanki07/prediccion-mundial-2026-cuartos-final
- Miguel Angel Marreros Cortegana: colocar enlace
- Valentin Fernandez Campos: colocar enlace
- Frank Salon Trigoso: colocar enlace
- Maria Carmen Tuesta Chuquizuta: colocar enlace

---

## Descripción general

El proyecto parte de la entrega previa de octavos de final y genera una nueva etapa para **cuartos de final**.

El flujo toma los clasificados a cuartos, construye los nuevos cruces, genera variables actualizadas para cada equipo y aplica el modelo predictivo usando:

```text
- Forma reciente.
- Goles a favor y en contra.
- Puntos recientes.
- Ranking FIFA.
- Ranking Elo.
- Historial entre selecciones.
- Contexto de eliminatoria.
- Fair Play y tarjetas.
- Poisson + Dixon-Coles.
```

---

## Objetivo general

Construir un modelo predictivo para los partidos de cuartos de final del Mundial 2026, capaz de estimar marcadores probables, probabilidades de clasificación a semifinales y posibles tarjetas por equipo.

---

## Objetivos específicos

- Crear los fixtures de cuartos a partir de los clasificados de octavos.
- Actualizar la base del modelo con resultados reales y predichos de octavos.
- Generar variables actualizadas para los partidos de cuartos.
- Estimar goles esperados mediante modelos entrenados.
- Calcular probabilidades de marcadores mediante Poisson.
- Ajustar marcadores bajos con Dixon-Coles.
- Estimar los clasificados a semifinales.
- Analizar posibles tarjetas usando datos de Fair Play.
- Mostrar las métricas de los modelos utilizados.

---

## Nota sobre los clasificados usados

El repositorio usa:

```text
- Resultados reales de octavos cuando el partido ya se jugó.
- Predicciones del modelo para los partidos de octavos que todavía estaban pendientes.
```

Por eso, algunos cruces de cuartos pueden aparecer como escenario predictivo si todavía no se contaba con todos los resultados reales al momento de la entrega.

---

## Modelos evaluados

En el proyecto se evaluaron cinco modelos:

```text
1. Regresión Lineal
2. Ridge Regression
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. Poisson Regressor
```

Las métricas están guardadas en:

```text
outputs/competencia_modelos.csv
outputs/resumen_metricas_modelos.csv
outputs/mejor_modelo.txt
```

Para la evaluación rápida no se recomienda volver a entrenar, porque el entrenamiento puede demorar. Se usan los modelos previamente entrenados y guardados.

---

## Modelo probabilístico

Para convertir los goles esperados en probabilidades de marcadores se usa una matriz de Poisson:

```text
P(Home = a) = (e^(-λ_home) * λ_home^a) / a!
P(Away = b) = (e^(-λ_away) * λ_away^b) / b!
P(a,b) = P(Home=a) * P(Away=b)
```

Donde:

```text
λ_home = goles esperados del equipo local
λ_away = goles esperados del equipo visitante
```

Luego se aplica la corrección Dixon-Coles para ajustar marcadores bajos:

```text
0-0
1-0
0-1
1-1
```

---

## Estructura principal del repositorio

```text
.
├── README.md
├── requirements.txt
├── 01_construir_data_modelo.py
├── 02_entrenar_predecir_modelos.py
├── 09_actualizar_fixtures_modelo_eliminatorias.py
├── 10_ver_metricas_modelos.py
├── 11_crear_fixtures_cuartos.py
├── 12_actualizar_fixtures_modelo_cuartos.py
├── 13_predecir_semifinales.py
├── data
│   ├── results.csv
│   ├── data_modelo.csv
│   ├── fair_play.csv
│   ├── fixtures_16avos.csv
│   ├── fixtures_octavos.csv
│   ├── fixtures_cuartos.csv
│   ├── fixtures_cuartos_modelo.csv
│   └── results_actualizado_cuartos.csv
└── outputs
    ├── competencia_modelos.csv
    ├── mejor_modelo.txt
    ├── resumen_metricas_modelos.csv
    ├── prediccion_octavos_a_cuartos.csv
    ├── clasificados_cuartos.csv
    ├── prediccion_cuartos_a_semifinales.csv
    ├── top10_marcadores_cuartos.csv
    ├── prediccion_tarjetas_cuartos.csv
    ├── clasificados_semifinales.csv
    ├── panel_metricas_modelos.png
    └── panel_cuartos_marcadores_tarjetas.png
```

---

## Scripts principales para esta entrega

### 11_crear_fixtures_cuartos.py

Crea el archivo:

```text
data/fixtures_cuartos.csv
```

Este script toma como base:

```text
outputs/clasificados_cuartos.csv
```

y genera los cruces de cuartos de final.

---

### 12_actualizar_fixtures_modelo_cuartos.py

Construye el archivo de variables para los partidos de cuartos:

```text
data/fixtures_cuartos_modelo.csv
```

También genera:

```text
data/results_actualizado_cuartos.csv
data/fixtures_modelo_actualizado_cuartos.csv
```

---

### 13_predecir_semifinales.py

Script principal de la entrega de cuartos.

Predice los partidos de cuartos y determina qué selecciones clasifican a semifinales.

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

Muestra las métricas de los modelos ya entrenados sin volver a entrenar.

Genera:

```text
outputs/resumen_metricas_modelos.csv
outputs/panel_metricas_modelos.png
```

---

# Instrucciones para evaluación del profesor

## 1. Clonar el repositorio

```bash
git clone https://github.com/Jeanki07/prediccion-mundial-2026-cuartos-final.git
cd prediccion-mundial-2026-cuartos-final
```

---

## 2. Crear entorno virtual

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

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si alguna dependencia falta, instalar:

```bash
pip install pandas numpy matplotlib scikit-learn joblib scipy
```

---

## 4. Ejecutar el proyecto

Orden recomendado:

```bash
python 11_crear_fixtures_cuartos.py
python 12_actualizar_fixtures_modelo_cuartos.py
python 13_predecir_semifinales.py
python 10_ver_metricas_modelos.py
```

---

## 5. Ver resultados desde terminal

### Predicción principal de cuartos

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/prediccion_cuartos_a_semifinales.csv'); print(df.to_string(index=False))"
```

### Top 10 marcadores probables

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/top10_marcadores_cuartos.csv'); print(df.to_string(index=False))"
```

### Predicción de tarjetas

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/prediccion_tarjetas_cuartos.csv'); print(df.to_string(index=False))"
```

### Clasificados a semifinales

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/clasificados_semifinales.csv'); print(df.to_string(index=False))"
```

### Métricas de modelos

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/resumen_metricas_modelos.csv'); print(df.to_string(index=False))"
```

---

## 6. Abrir paneles visuales

En Linux:

```bash
xdg-open outputs/panel_cuartos_marcadores_tarjetas.png
xdg-open outputs/panel_metricas_modelos.png
```

En Windows o macOS, abrir manualmente los archivos `.png` desde la carpeta `outputs`.

---

## Resultados generados

```text
outputs/prediccion_cuartos_a_semifinales.csv
outputs/top10_marcadores_cuartos.csv
outputs/prediccion_tarjetas_cuartos.csv
outputs/clasificados_semifinales.csv
outputs/panel_cuartos_marcadores_tarjetas.png
outputs/resumen_metricas_modelos.csv
outputs/panel_metricas_modelos.png
```

---

## Nota sobre entrenamiento

El entrenamiento completo se realizó previamente con:

```text
02_entrenar_predecir_modelos.py
```

Ese script entrena los cinco modelos y puede demorar. Para esta entrega se recomienda ejecutar directamente los scripts de cuartos, porque los modelos ya están guardados en la carpeta `outputs`.

---

## Comando rápido de evaluación

```bash
git clone https://github.com/Jeanki07/prediccion-mundial-2026-cuartos-final.git
cd prediccion-mundial-2026-cuartos-final
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python 11_crear_fixtures_cuartos.py
python 12_actualizar_fixtures_modelo_cuartos.py
python 13_predecir_semifinales.py
python 10_ver_metricas_modelos.py
```

En Windows, reemplazar:

```bash
source venv/bin/activate
```

por:

```bash
venv\Scripts\activate
```

---

## Estado de la entrega

Este repositorio debe mantenerse como versión específica para la fase de **cuartos de final**.  
No se recomienda actualizarlo con semifinales o fases posteriores dentro del mismo repositorio.
