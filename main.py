import os, psycopg

DATABASE_URL = 

url = os.getenv("DATABASE_URL")

try:
    # CONEXIÓN A LA BASE DE DATOS
    connection = psycopg.connect(url)

    #CURSOR
    cur = connection.cursor()
    print("Base de datos conectada con éxito")
except Exception as e:
    print("Error conectando a la base de datos:", e)

query = " SELECT id, name, species from characters"