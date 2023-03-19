# Proyecto Individual Henry Nº1
  #   Milton Aquino

# INTRODUCCIÓN

El proyecto consistía en situarse en el rol de Data Engineer, a quien como miembro del equipo de una empresa, el Tech Lead le solicita realizar un proceso de ETL sobre cuatro datasets proporcionados, conteniendo información relativa a los catálogos de series y películas de cuatro plataformas de streaming (Netflix, Hulu, Amazon Prime Video y Disney).

Como segunda parte del requerimiento, se solicitaba elaborar una API a efectos de disponibilizar los datos de manera online, los cuales debían ser accedidos mediante cinco consultas predefinidas.

Por último, se solicita documentar todo el proceso y el funcionamiento de la API, y efectuar un video que sería remitido al Tech Lead que nos encargó el proyecto para que nos efectúe un feedback sobre el mismo.

# Propuesta de trabajo (requerimientos de aprobación)

Transformaciones: Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Vas a hacer estas, y solo estas, transformaciones a los datos:

Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

De haber fechas, deberán tener el formato AAAA-mm-dd

Los campos de texto deberán estar en minúsculas, sin excepciones

El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)


Desarrollo API: Propones disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:

Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))


Deployment: Conoces sobre Render y tienes un tutorial de Render que te hace la vida mas facil 😄 . Tambien podrias usar Railway, pero ten en cuenta que con este si necesitas dockerizacion.


Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente 👀 ), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Sabes que puedes apoyarte en librerías como pandas profiling, sweetviz, autoviz, entre otros y sacar de allí tus conclusiones 😉

Sistema de recomendación:

Una vez que toda la data es consumible por la API ya lista para consumir para los departamentos de Analytics y de Machine Learning, y nuestro EDA bien realizado entendiendo bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas para usuarios, donde dado un id de usuario y una película, nos diga si la recomienda o no para dicho usuario. De ser posible, este sistema de recomendación debe ser deployado para tener una interfaz gráfica amigable para ser utilizada, utilizando Gradio para su deployment o bien con alguna solución como Streamlit o algo similar en local (tener el deployment del sistema de recomendación o una interfaz gráfica es un plus al proyecto).

Video: Necesitas que al equipo le quede claro que tus herramientas funcionan realmente! Haces un video mostrando el resultado de las consultas propuestas y de tu modelo de ML entrenado!

# Tareas realizadas:
  #   API
https://deploy-proyectohenry-final.onrender.com/docs
 # Video de demostración 
 https://youtu.be/a4jGb071VvM
