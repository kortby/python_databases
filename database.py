import sqlalchemy as db

engine = db.create_engine('sqlite:///movies.db')

connection = engine.connect()
metadata = db.MetaData()

movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

# selecting all
# query = db.select([movies])

# selecting where it match
# query = db.select([movies]).where(movies.columns.Director == 'Martin Scorsese')

# insert in the data

# result_proxy = connection.execute(query)

# result_set = result_proxy.fetchall()

# print(result_set[0])
# print(result_set[:2])
# print('------------------------------')


query = movies.insert().values(Title='Psycho', Director='Alfred Hitchcock', Year=1983)
connection.execute(query)
query = db.select([movies])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)
