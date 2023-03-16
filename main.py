from fastapi import FastAPI
import pandas as pd


app = FastAPI( title="Películas y Series")

@app.get ("/")
async def read_root():
    return {"******* Hola, Mi nombre es Milton!! Este es mi Proyecto Nª 1 para Henry. ******"}


#Consultas

'''
1. Cantidad de veces que aparece una keyword en el título de
 peliculas/series, por plataforma.
'''
@app.get("/get_word_count")
def get_word_count(plataforma: str, keyword: str):
    movie_df=pd.read_csv('pelis_score')
    #pasamos las entradas a minúsculas
    plataforma =plataforma.lower()
    keyword=keyword.lower()
    #creamos la columna 'platform' 
    movie_df['platform']=movie_df['id'].str[0]
    #filtramos por plataforma
    platform_df = movie_df[movie_df['platform'] == plataforma[0]]
    #extramos los titulos en dicha plataforma 
    titles = platform_df['title']
    #luego iteramos a través de los títulos de las filas filtradas
    count = 0
    for title in titles:
        count += title.count(keyword)
    return f"La keyword '{keyword}' aparece {count} veces en los títulos de películas y series de la plataforma {plataforma}."

