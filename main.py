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
]

try:
  with psycopg.connect(url) as connection:
    print("Base de datos conectada con éxito")

    with connection.cursor() as cur:
      # 1. Crear la tabla si no existe
      cur.execute("""
                CREATE TABLE IF NOT EXISTS personajes (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    status VARCHAR(50),
                    species VARCHAR(100),
                    type VARCHAR(100),
                    gender VARCHAR(50),
                    origin_name VARCHAR(100),
                    location_name VARCHAR(100)
                );
            """)

      # 2. Insertar los datos
      insert_query = """
                INSERT INTO personajes (name, status, species, type, gender, origin_name, location_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
      cur.executemany(insert_query, personajes)

      print(f"Se insertaron {len(personajes)} personajes correctamente.")

      # 3. Ver datos de la tabla (dentro del mismo cursor)
      cur.execute("SELECT * FROM personajes;")
      filas = cur.fetchall()

      print("\n--- REGISTROS EN LA TABLA PERSONAJES ---")
      for fila in filas:
        print(fila) 

except Exception as e:
  print(f"Error al insertar los datos: {e}")