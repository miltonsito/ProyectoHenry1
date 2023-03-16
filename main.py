from fastapi import FastAPI
import pandas as pd


app = FastAPI( title="Películas y Series")

@app.get ("/")
async def read_root():
    return {"******* Hola, Mi nombre es Milton!! Este es mi Proyecto Nº 1 para Henry. ******"}


#Consultas

'''
Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. 
(la función debe llamarse get_max_duration(year, platform, duration_type))
'''
# Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN
@app.get("/get_max_duration")
def get_max_duration(year: int, platform: str, duration_type: str):
    movie_df=pd.read_csv('pelis_score1.csv')
    # Filtrar los datos según los parámetros recibidos
    filtered_df = movie_df.copy()
    if year:
        filtered_df = filtered_df[filtered_df.Year == year]
    if platform:
        filtered_df = filtered_df[filtered_df.Platform == platform]
    if duration_type:
        filtered_df = filtered_df[filtered_df.Duration == duration_type]

    # Encontrar la película con mayor duración en el dataframe filtrado
    max_duration_movie = filtered_df[filtered_df.Duration == filtered_df.Duration.max()].iloc[0]

    # Devolver el título de la película con mayor duración y su duración
    return {"title": max_duration_movie.Title, "duration": max_duration_movie.Duration}

