import psycopg2

conn = psycopg2.connect(
    """
    dbname=mysite user=postgres host=localhost port=5432
    """
)
conn.set_session(autocommit=True)

cur = conn.cursor()



# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS races cascade;
    """
)

cur.execute(
    """
    DROP TABLE IF EXISTS incident cascade;
    """
)

cur.execute(
    """
    DROP TABLE IF EXISTS drivers cascade;
    """
)

cur.execute(
    """
    DROP TABLE IF EXISTS cars cascade;
    """
)

cur.execute(
    """
    CREATE TABLE races (
    id SERIAL PRIMARY KEY,
    starting_position INT NOT NULL UNIQUE,
    ending_position INT NOT NULL UNIQUE,
    qualifying_time INT,
    average_lap_times INT NOT NULL,
    best_lap_times INT NOT NULL
    )
    """
)

cur.execute(
    """
    INSERT INTO races VALUES
    (1, 1, 1, 28.674 , 30.004, 28.794),
    (2, 4, 2, 28.736, 30.072, 28.758),
    (3, 5, 3, 28.763, 30.161, 28.990),
    (4, 3, 4, 28.793, 30.167, 29.161),
    (5, 2, 5, 28.844, 30.223, 28.784),
    (6, 8, 6, 28.898, 30.335, 29.220),
    (7, 16, 7, 28.925, 30.592, 29.281),
    (8, 22, 8, 28.942, 30.625, 29.452),
    (9, 19, 9, 29.027, 30.684, 29.046),
    (10, 12, 10, 29.049, 30.839, 28.906),
    (11, 20, 11, 29.145, 31.016, 29.504),
    (12, 21, 12, 29.242, 31.351, 29.377),
    (13, 18, 13, 29.294, 31.677, 29.649),
    (14, 7, 14, 29.429, 31.845, 29.307),
    (15, 17, 15, 29.571, 32.182, 29.812)
    """
)

cur.execute(
    """
    CREATE TABLE incident (
    id SERIAL PRIMARY KEY,
    cars_involved INT NOT NULL,
    number_of_incidents INT NOT NULL
    )
    """
)

cur.execute(
    """
    INSERT INTO incident VALUES
    (1, 0, 0),
    (2, 2, 2),
    (3, 0, 0),
    (4, 0, 0),
    (5, 0, 0),
    (6, 0, 0),
    (7, 1, 2),
    (8, 0, 0),
    (9, 2, 4),
    (10, 3, 8),
    (11, 4, 8),
    (12, 0, 0),
    (13, 0, 0),
    (14, 3, 4),
    (15, 6, 9)
    """
)


################################################

cur.execute(
    """
    CREATE TABLE drivers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email_address TEXT UNIQUE
    )
    """
)



cur.execute(
    """
    INSERT INTO drivers VALUES
    (1, 'joe backus', 12345, null),
    (2, 'william vining', 51234, null),
    (3, 'nahuel diaz caviglia', 61235, null),
    (4, 'andy wilkinson', 53116 , null),
    (5, 'william miller', 123567, null),
    (6, 'nathan stevens', 09843, null),
    (7, 'dylan steinkruger', 6547, null),
    (8, 'robert rushing', 7634, null),
    (9, 'eric miller', 8563, null),
    (10, 'chi kuba', 7653, null),
    (11, 'tyler shackelford', 765357, null),
    (12, 'mathew sichette', 8352, null),
    (13, 'justin wilkes', 2345, null),
    (14, 'jason roy alvarez', 5324, null),
    (15, 'christopher trower', 46781, null)
    """
)


#######################################

cur.execute(
    """
    CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    license TEXT NOT NULL,
    year INT,
    make TEXT NOT NULL,
    model TEXT NOT NULL
    )
    """
)


cur.execute(
    """
    INSERT INTO cars VALUES
    (1, 'a', 1953, 'toyota', 'arca'),
    (2, 'a', 1953, 'toyota', 'arca'),
    (3, 'c', 1953, 'chevrolet', 'arca'),
    (4, 'd', 1953, 'ford', 'arca'),
    (5, 'c', 1953, 'chevrolet', 'arca'),
    (6, 'a', 1953, 'toyota', 'arca'),
    (7, 'd', 1953, 'ford', 'arca'),
    (8, 'd', 1953, 'toyota', 'arca'),
    (9, 'c', 1953, 'ford', 'arca'),
    (10, 'b', 1953, 'toyota', 'arca'),
    (11, 'b', 1953, 'ford', 'arca'),
    (12, 'd', 1953, 'toyota', 'arca'),
    (13, 'b', 1953, 'chevrolet', 'arca'),
    (14, 'd', 1953, 'toyota', 'arca'),
    (15, 'd', 1953, 'chevrolet', 'arca')
    """
)


# Execute query

cur.execute(
    """
    SELECT * FROM Races
    """
)
cur.execute(
    """
    SELECT * FROM Drivers
    """
)
cur.execute(
    """
    SELECT * FROM Incident
    """
)

#Retrieve query results
records = cur.fetchall()

print(records)

