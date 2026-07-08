# ============================================================
# 11_crear_fixtures_cuartos.py
# Crea data/fixtures_cuartos.csv a partir de outputs/clasificados_cuartos.csv.
#
# Usa clasificados reales cuando el partido de octavos ya se jugó
# y clasificados predichos cuando el partido todavía estaba pendiente.
# ============================================================

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUT_DIR = BASE_DIR / "outputs"

ARCHIVO_CLASIFICADOS_CUARTOS = OUT_DIR / "clasificados_cuartos.csv"
ARCHIVO_PREDICCION_OCTAVOS = OUT_DIR / "prediccion_octavos_a_cuartos.csv"
ARCHIVO_FIXTURES_CUARTOS = DATA_DIR / "fixtures_cuartos.csv"


def leer_csv(ruta):
    if not ruta.exists():
        raise FileNotFoundError("No existe el archivo: " + str(ruta))

    df = pd.read_csv(ruta)
    df.columns = df.columns.str.strip()
    return df


def obtener_clasificados():
    if ARCHIVO_CLASIFICADOS_CUARTOS.exists():
        df = leer_csv(ARCHIVO_CLASIFICADOS_CUARTOS)

        if "match_id_octavos" in df.columns and "team" in df.columns:
            df["match_id_octavos"] = pd.to_numeric(
                df["match_id_octavos"],
                errors="coerce"
            ).astype("Int64")

            return {
                int(fila["match_id_octavos"]): {
                    "team": fila["team"],
                    "source": fila.get("source", "DESCONOCIDO")
                }
                for _, fila in df.dropna(subset=["match_id_octavos"]).iterrows()
            }

    pred = leer_csv(ARCHIVO_PREDICCION_OCTAVOS)

    if "final_winner" not in pred.columns:
        raise ValueError("No se encontró columna final_winner en prediccion_octavos_a_cuartos.csv")

    pred["match_id"] = pd.to_numeric(pred["match_id"], errors="coerce").astype("Int64")

    return {
        int(fila["match_id"]): {
            "team": fila["final_winner"],
            "source": fila.get("source", "DESCONOCIDO")
        }
        for _, fila in pred.dropna(subset=["match_id"]).iterrows()
    }


def equipo(clasificados, match_id):
    if match_id not in clasificados:
        raise ValueError(f"No se encontró clasificado del partido de octavos {match_id}")

    return clasificados[match_id]["team"]


def fuente(clasificados, match_id):
    if match_id not in clasificados:
        return "DESCONOCIDO"

    return clasificados[match_id]["source"]


def main():
    clasificados = obtener_clasificados()

    # Estructura del cuadro:
    # 97 = ganador 90 vs ganador 89
    # 98 = ganador 93 vs ganador 94
    # 99 = ganador 91 vs ganador 92
    # 100 = ganador 95 vs ganador 96
    fixtures = [
        {
            "match_id": 97,
            "date": "2026-07-09",
            "round": "CUARTOS",
            "home_team": equipo(clasificados, 90),
            "away_team": equipo(clasificados, 89),
            "home_score": "",
            "away_score": "",
            "pen_home": "",
            "pen_away": "",
            "source_note": f"Generado desde octavos: 90={fuente(clasificados, 90)} / 89={fuente(clasificados, 89)}"
        },
        {
            "match_id": 98,
            "date": "2026-07-10",
            "round": "CUARTOS",
            "home_team": equipo(clasificados, 93),
            "away_team": equipo(clasificados, 94),
            "home_score": "",
            "away_score": "",
            "pen_home": "",
            "pen_away": "",
            "source_note": f"Generado desde octavos: 93={fuente(clasificados, 93)} / 94={fuente(clasificados, 94)}"
        },
        {
            "match_id": 99,
            "date": "2026-07-11",
            "round": "CUARTOS",
            "home_team": equipo(clasificados, 91),
            "away_team": equipo(clasificados, 92),
            "home_score": "",
            "away_score": "",
            "pen_home": "",
            "pen_away": "",
            "source_note": f"Generado desde octavos: 91={fuente(clasificados, 91)} / 92={fuente(clasificados, 92)}"
        },
        {
            "match_id": 100,
            "date": "2026-07-11",
            "round": "CUARTOS",
            "home_team": equipo(clasificados, 95),
            "away_team": equipo(clasificados, 96),
            "home_score": "",
            "away_score": "",
            "pen_home": "",
            "pen_away": "",
            "source_note": f"Generado desde octavos: 95={fuente(clasificados, 95)} / 96={fuente(clasificados, 96)}"
        }
    ]

    df = pd.DataFrame(fixtures)

    DATA_DIR.mkdir(exist_ok=True)
    df.to_csv(ARCHIVO_FIXTURES_CUARTOS, index=False, encoding="utf-8")

    print()
    print("========================================")
    print("FIXTURES DE CUARTOS GENERADOS")
    print("========================================")
    print(df.to_string(index=False))
    print()
    print("Archivo generado:")
    print(ARCHIVO_FIXTURES_CUARTOS)
    print("========================================")


if __name__ == "__main__":
    main()
