from sqlite3.dbapi2 import Cursor
import mysql.connector as mysql
import csv

connection = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='sales'
)

cursor = connection.cursor()

create_query = ''' 
CREATE TABLE salesperson(
    id INT(255) NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(200) NOT NULL,
    lastname  VARCHAR(200) NOT NULL,
    email  VARCHAR(200) NOT NULL,
    city  VARCHAR(200) NOT NULL,
    state  VARCHAR(200) NOT NULL,
    PRIMARY KEY (id)
    ) 
'''

cursor.execute('DROP TABLE IF EXISTS salesperson')

cursor.execute(create_query)

with open('./salespeople.csv', 'r') as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        row_tuple = tuple(row)
        cursor.execute(
            'INSERT INTO salesperson(firstname, lastname, email, city, state) VALUES ("%s", "%s", "%s", "%s", "%s")', row_tuple)

connection.commit()

cursor.execute('SELECT * FROM salesperson LIMIT 10')
print(cursor.fetchall())

connection.close()
