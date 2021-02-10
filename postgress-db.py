import psycopg2


con = psycopg2.connect(
    database='red30',
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
)

cursor = con.cursor()

cursor.execute(
    ''' CREATE TABLE Sales (ORDER_NUM INT PRIMARY KEY, ORDER_TYPE TEXT))''')
