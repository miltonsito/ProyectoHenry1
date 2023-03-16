from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Películas y Series")

@app.get("/")
async def read_root():
    return {"******* Hola, Mi nombre es Milton!! Este es mi Proyecto Nº 1 para Henry. ******"}

# Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN
@app.get("/get_max_duration")
def get_max_duration(year: int, platform: str, duration_type: str):
    movie_df = pd.read_csv('pelis_score.or.csv')
    # Filtrar los datos según los parámetros recibidos
    filtered_df = movie_df
    if year:
        filtered_df = filtered_df[filtered_df.Year == year]
    if platform:
        filtered_df = filtered_df[filtered_df.Platform == platform]
    if duration_type:
        filtered_df = filtered_df[filtered_df.Duration == duration_type]

    # Encontrar la película con mayor duración en el dataframe filtrado
    max_duration = filtered_df['duration_int'].max()
    max_duration_movie = filtered_df[filtered_df['duration_int'] == max_duration].iloc[0]

    # Devolver el título de la película con mayor duración y su duración
    return {"title": max_duration_movie["title"], "duration_int": max_duration_movie["duration_int"]}

