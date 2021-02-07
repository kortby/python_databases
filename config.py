from os import access
import sqlite3

connection = sqlite3.connect('movies.db')

# with this cursor we can access commands in database
cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Movies
(Title TEXT, Director TEXT, Year INT) ''')

famousFilms = [
    ('Pulp Fiction', 'Quentin Tarantino', 1994),
    ('Back to the future', 'Steven Spielberg', 1985),
    ('Moonrise Kingdom', 'Wes Anderson', 2012),
]

cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousFilms)

cursor.execute(
    "INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")
records = cursor.execute("SELECT * FROM Movies")

print('-----------------')
release_year = (1985,)
cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

print(cursor.fetchall())


connection.commit()
connection.close()
