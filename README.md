# Modelo predictivo para cuartos de final del Mundial 2026

Repositorio de entrega para el **modelo predictivo de cuartos de final del Mundial FIFA 2026**.

Esta versión recupera la estructura completa del proyecto original: resultados oficiales, marcadores, tarjetas, ranking FIFA, ranking Elo, contexto del partido, competencia de modelos y visualización integral.

---

## Integrantes del grupo

- Jean Frank Bustamante Vela
- Miguel Angel Marreros Cortegana
- Valentin Fernandez Campos
- Frank Salon Trigoso
- Maria Carmen Tuesta Chuquizuta

---

## Enlace individual de GitHub

- Jean Frank Bustamante Vela: https://github.com/Jeanki07/prediccion-mundial-2026-cuartos-final
- Miguel Angel Marreros Cortegana: colocar enlace
- Valentin Fernandez Campos: colocar enlace
- Frank Salon Trigoso: colocar enlace
- Maria Carmen Tuesta Chuquizuta: colocar enlace

---

## Entrega

**Modelo predictivo para cuartos de final del Mundial 2026.**

El repositorio predice qué selecciones clasifican de **cuartos de final a semifinales** usando:

```text
- Resultados oficiales de octavos de final.
- Marcadores oficiales.
- Tarjetas oficiales por partido.
- Ranking FIFA.
- Ranking Elo.
- Forma reciente: goles a favor, goles en contra y puntos en últimos 12 partidos.
- Historial directo entre selecciones.
- Contexto de eliminatoria.
- Competencia de modelos.
- Poisson + Dixon-Coles.
- Fair Play y riesgo disciplinario.
```

---

## Resultados oficiales de octavos considerados

```text
Canada 0-3 Morocco
Paraguay 0-1 France
Brazil 1-2 Norway
Mexico 2-3 England
Portugal 0-1 Spain
United States 1-4 Belgium
Argentina 3-2 Egypt
Switzerland 0-0 Colombia, Switzerland gana 4-3 por penales
```

Por lo tanto, los cuartos de final quedan:

```text
France vs Morocco
Spain vs Belgium
Norway vs England
Argentina vs Switzerland
```

---

## Modelos evaluados

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

El script `10_ver_metricas_modelos.py` permite ver las métricas sin volver a entrenar.

---

## Scripts principales

### 00_actualizar_datos_oficiales.py

Actualiza la base oficial de la entrega:

```text
- data/fixtures_octavos.csv
- data/fixtures_cuartos.csv
- data/tarjetas_octavos_reales.csv
- data/fair_play.csv
- data/results.csv
- outputs/clasificados_cuartos.csv
- outputs/prediccion_octavos_a_cuartos.csv
```

---

### 12_actualizar_fixtures_modelo_cuartos.py

Construye las variables para cuartos de final:

```text
- data/fixtures_cuartos_modelo.csv
- data/results_actualizado_cuartos.csv
- data/fixtures_modelo_actualizado_cuartos.csv
```

---

### 13_predecir_semifinales.py

Predice los partidos de cuartos y genera:

```text
- outputs/prediccion_cuartos_a_semifinales.csv
- outputs/top10_marcadores_cuartos.csv
- outputs/prediccion_tarjetas_cuartos.csv
- outputs/clasificados_semifinales.csv
- outputs/panel_cuartos_marcadores_tarjetas.png
```

---

### 14_panel_integral_cuartos.py

Genera la visualización completa de la entrega:

```text
- outputs/analisis_contexto_cuartos.csv
- outputs/panel_competencia_modelos.png
- outputs/panel_integral_cuartos.png
```

Este panel muestra en una sola vista:

```text
- Ranking FIFA de ambos equipos.
- Ranking Elo de ambos equipos.
- Diferencia FIFA y Elo.
- Forma reciente.
- Lambdas finales.
- Probabilidades de clasificación.
- Marcador más probable.
- Clasificado predicho.
- Tarjetas esperadas.
- Riesgo disciplinario.
- Mejor modelo base.
```

---

## Instrucciones para el profesor

### 1. Clonar el repositorio

```bash
git clone https://github.com/Jeanki07/prediccion-mundial-2026-cuartos-final.git
cd prediccion-mundial-2026-cuartos-final
```

### 2. Crear entorno virtual

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la evaluación completa

```bash
python 00_actualizar_datos_oficiales.py
python 12_actualizar_fixtures_modelo_cuartos.py
python 13_predecir_semifinales.py
python 10_ver_metricas_modelos.py
python 14_panel_integral_cuartos.py
```

---

## Comando rápido de evaluación

```bash
git clone https://github.com/Jeanki07/prediccion-mundial-2026-cuartos-final.git
cd prediccion-mundial-2026-cuartos-final
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python 00_actualizar_datos_oficiales.py
python 12_actualizar_fixtures_modelo_cuartos.py
python 13_predecir_semifinales.py
python 10_ver_metricas_modelos.py
python 14_panel_integral_cuartos.py
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

## Archivos de salida principales

```text
outputs/prediccion_cuartos_a_semifinales.csv
outputs/top10_marcadores_cuartos.csv
outputs/prediccion_tarjetas_cuartos.csv
outputs/clasificados_semifinales.csv
outputs/resumen_metricas_modelos.csv
outputs/analisis_contexto_cuartos.csv
outputs/panel_cuartos_marcadores_tarjetas.png
outputs/panel_metricas_modelos.png
outputs/panel_competencia_modelos.png
outputs/panel_integral_cuartos.png
```

---

## Ver resultados por terminal

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/prediccion_cuartos_a_semifinales.csv'); print(df.to_string(index=False))"
```

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/analisis_contexto_cuartos.csv'); print(df.to_string(index=False))"
```

```bash
python -c "import pandas as pd; df=pd.read_csv('outputs/resumen_metricas_modelos.csv'); print(df.to_string(index=False))"
```

---

## Abrir visualizaciones

Linux:

```bash
xdg-open outputs/panel_integral_cuartos.png
xdg-open outputs/panel_competencia_modelos.png
xdg-open outputs/panel_cuartos_marcadores_tarjetas.png
```

Windows/macOS: abrir los archivos `.png` desde la carpeta `outputs`.

---

## Nota metodológica

La predicción no usa el marcador crudo de la regresión como resultado final. El modelo primero genera goles esperados o lambdas, luego las calibra con forma reciente, defensa rival, ranking FIFA, ranking Elo, historial directo y contexto de eliminatoria.

Después aplica una matriz de Poisson y corrección Dixon-Coles para marcadores bajos como:

```text
0-0
1-0
0-1
1-1
```

La parte disciplinaria se estima con Fair Play, tarjetas reales acumuladas y contexto de partido de eliminación directa.
