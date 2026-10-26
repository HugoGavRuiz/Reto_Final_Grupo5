CREATE TABLE characters (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT,
    status TEXT,
    species TEXT,
    type TEXT,
    gender TEXT,
    origin_name TEXT,
    location_name TEXT,
    image TEXT,
    url TEXT,
    created TIMESTAMPTZ
)

INSERT INTO characters (name, status, species, type, gender, origin_name, location_name)
VALUES (
    INSERT INTO characters (name, status, species, type, gender, origin_name, location_name)
VALUES
    ('Tony Stark', 'Dead', 'Human', 'Superhero', 'Male', 'Earth', 'Earth'),
    ('Steve Rogers', 'Alive', 'Human', 'Super soldier', 'Male', 'Earth', 'Earth'),
    ('Thor', 'Alive', 'Asgardian', 'God of Thunder', 'Male', 'Asgard', 'New Asgard'),
    ('Natasha Romanoff', 'Dead', 'Human', 'Spy', 'Female', 'Earth', 'Earth'),
    ('Bruce Banner', 'Alive', 'Human', 'Scientist', 'Male', 'Earth', 'Earth'),
    ('Clint Barton', 'Alive', 'Human', 'Archer', 'Male', 'Earth', 'Earth'),
    ('Wanda Maximoff', 'Alive', 'Human', 'Enhanced', 'Female', 'Sokovia', 'Earth'),
    ('Peter Parker', 'Alive', 'Human', 'Superhero', 'Male', 'Earth', 'Earth'),
    ('Doctor Strange', 'Alive', 'Human', 'Sorcerer', 'Male', 'Earth', 'Kamar-Taj'),
    ('Thanos', 'Dead', 'Titan', 'Villain', 'Male', 'Titan', 'The Garden');
)