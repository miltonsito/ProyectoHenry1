from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Películas y Series")

@app.get("/")
async def read_root():
     return {"******* Hola, Mi nombre es Milton!! Este es mi Proyecto Nº 1 para Henry. ******"}

#Película con mayor duración con filtros opcionales de 
#AÑO, PLATAFORMA Y TIPO DE DURACIÓN.


@app.get("/get_max_duration")
async def get_max_duration(year: int, platform: str, duration_type: str):
    
    
    df = pd.read_csv('pelis_score.or.csv')
    # Filtro las columnas
    filtered_df = df.loc[(df["year"] == year if year else True) &
                         (df["platform"] == platform if platform else True) &
                         (df["duration_type"] == duration_type if duration_type else True)]

    # Encontrar la película con la mayor duración
    max_duration_movie = filtered_df.loc[filtered_df["duration_int"].idxmax()]

    return max_duration_movie["title"]

'''
Cantidad de películas 
por plataforma con un puntaje mayor a XX en determinado año
'''


@app.get("/get_score_count")
def get_score_count(platform: str, scored: float, year: int) -> int:
    df = pd.read_csv('pelis_score.or.csv')
    
    # Filtrar el dataframe según la plataforma y el año
    filtered_df = df.loc[(df["platform"] == platform) & (df["year"] == year)]

    # Contar la cantidad de películas con un puntaje mayor a "scored"
    cantidad_peli = filtered_df.loc[filtered_df["score"] > scored].groupby("platform")["title"].count()[platform]

    return cantidad_peli

'''
Cantidad de películas por 
plataforma con filtro de PLATAFORMA.
'''

@app.get("/get_count_platform")
async def get_count_platform(platform: str) -> int:
    df = pd.read_csv('pelis_score.or.csv')
    
    # Filtrar el dataframe según la plataforma
    filtered_df = df[df['platform'] == platform]

    # Contar la cantidad de películas por plataforma
    cantidad_plat = filtered_df.groupby('platform')['title'].count()[0]

    return cantidad_plat

'''
Actor que más se repite según plataforma y año
'''

@app.get("/get_actor")
async def get_actor(platform: str, year: int):

    df = pd.read_csv('pelis_score.or.csv')

    # Filtrar el dataframe según la plataforma y el año
    filtered_df = df[(df['platform'] == platform) & (df['year'] == year)]

    # Dividir la cadena de actores en una lista y convertir en un dataframe
    actors_df = filtered_df['cast'].str.split(', ', expand=True)

    # Obtener el actor que más se repite
    actor_count = actors_df.stack().value_counts().reset_index()
    actor_repe = actor_count.iloc[0]['index']

    return actor_repe



