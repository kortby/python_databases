import sqlite3

connection = sqlite3.connect('user-sqlite.db')

cursor = connection.cursor()


cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Users
(user_id INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, email TEXT) 
''')

usersToInsert = [
    ('Tina', 'Mccoy', 'tinamoccoy@example.com'),
    ('John', 'Doe', 'johndoe@example.com'),
    ('Sara', 'Cox', 'saracox@example.com'),
    ('Jessica', 'Alvarez', 'jessicaalvares@example.com'),
]

cursor.executemany(
    ''' INSERT INTO Users(firstname, lastname, email) VALUES (?,?,?)''', usersToInsert)

cursor.execute('SELECT email FROM Users')

print(cursor.fetchall())

cursor.execute('SELECT * FROM Users')
print(cursor.fetchall())


connection.commit()
connection.close()
