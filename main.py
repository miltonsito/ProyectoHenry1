from fastapi import FastAPI
import pandas as pd


app = FastAPI( title="Películas y Series",
    description="Esta API permite realizar consultas de diferentes plataformas",
    version='0.0.1')

pelis_series = pd.read_csv("movies_datos.csv")
rating_score = pd.read_csv("rating_score.csv")

@app.get("/")
def index():
    return "Este es el Proyecto Individual Nº 1"

@app.get("/max_duration_movie")
def max_duration_movie(year: int = None, platform: str = None, duration_type: str = None):
    return {"data": get_max_duration(year, platform, duration_type)}

