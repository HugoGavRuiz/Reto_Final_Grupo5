import os, psycopg

url = os.getenv("DATABASE_URL")

personajes = [
    ('Tony Stark', 'Dead', 'Human', 'Superhero', 'Male', 'Earth', 'Earth'),
    ('Steve Rogers', 'Alive', 'Human', 'Super soldier', 'Male', 'Earth', 'Earth'),
    ('Thor', 'Alive', 'Asgardian', 'God of Thunder', 'Male', 'Asgard', 'New Asgard'),
    ('Natasha Romanoff', 'Dead', 'Human', 'Spy', 'Female', 'Earth', 'Earth'),
    ('Bruce Banner', 'Alive', 'Human', 'Scientist', 'Male', 'Earth', 'Earth'),
    ('Clint Barton', 'Alive', 'Human', 'Archer', 'Male', 'Earth', 'Earth'),
    ('Wanda Maximoff', 'Alive', 'Human', 'Enhanced', 'Female', 'Sokovia', 'Earth'),
    ('Peter Parker', 'Alive', 'Human', 'Superhero', 'Male', 'Earth', 'Earth'),
    ('Doctor Strange', 'Alive', 'Human', 'Sorcerer', 'Male', 'Earth', 'Kamar-Taj'),
    ('Thanos', 'Dead', 'Titan', 'Villain', 'Male', 'Titan', 'The Garden'),
]

try:
    # CONEXIÓN A LA BASE DE DATOS
    with psycopg.connect(url) as connection:
        # CURSOR
        with connection.cursor() as cur:
            query = """
            INSERT INTO characters
                (name, status, species, type, gender, origin_name, location_name)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.executemany(query, personajes)
    print("Personajes insertados con éxito")

      # COMPROBAR CON UN SELECT (conexión nueva, los datos ya están guardados)
    with psycopg.connect(url) as connection:
        with connection.cursor() as cur:
            cur.execute("SELECT id, name, status, species FROM characters ORDER BY id")
            filas = cur.fetchall()

    print(f"La tabla characters tiene {len(filas)} filas:")
    for fila in filas:
        print(fila)
        
except Exception as e:
    print("Error conectando a la base de datos:", e)