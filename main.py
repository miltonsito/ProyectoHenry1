from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Películas y Series")

@app.get("/")
async def read_root():
     return {"******* Hola, Mi nombre es Milton!! Este es mi Proyecto Nº 1 para Henry. ******"}


@app.get("/get_max_duration")
async def get_max_duration(year: int, platform: str, duration_type: str):
    
    import pandas as pd
    data_plataformas = pd.read_csv('pelis_score.or.csv', sep=',')

    # 1. Filtro por año
    filtro_anio = data_plataformas.loc[ data_plataformas['year'] == year ]

    # 2. Filtro por plataforma
    # a: amazon, d: disney, h: hulu, n: netflix
    filtro_plataforma = filtro_anio.loc[ filtro_anio['platform'] == platform ]

    # 3. Filtro por tipo de duracion
    filtro_tipo_duracion = filtro_plataforma.loc[ filtro_plataforma['duration_type'] == duration_type ]

    # 4. Filtro de mayor duracion
    max_duracion = filtro_tipo_duracion.loc[ filtro_tipo_duracion['duration_int'] == filtro_tipo_duracion['duration_int'].max() ]
    
    max_duracion_movie = max_duracion.iloc[0]
    movie_max_duracion = max_duracion['title']
    max_duracion_duration = max_duracion_movie['duration_int']

    
    return {"title": max_duracion_title, "duration_int": max_duracion_duration}


