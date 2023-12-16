from sqlalchemy import create_engine, text
import time

def q_SQLAlchemy(q, k):
    start = time.time()
    for i in range(10):
        conn.execute(text(q))
    end = time.time()
    print("The time Q", k, "is :", (end - start) / 10, "s")

Q = ['''SELECT "VendorID", COUNT(*) FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", AVG("total_amount")FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*) FROM table_name GROUP BY 1, 2''',
     '''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*) 
     FROM table_name GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;''']

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
conn = engine.connect()

q_SQLAlchemy(Q[0], 1)
q_SQLAlchemy(Q[1], 2)
q_SQLAlchemy(Q[2], 3)
q_SQLAlchemy(Q[3], 4)

"""
print('querry1')
r = conn.execute(text('''SELECT "VendorID", COUNT(*) FROM table_name GROUP BY 1'''))
r = r.all()
for row in r:
    print(row)
print('querry2')
r = conn.execute(text('''SELECT "passenger_count", AVG("total_amount")FROM table_name GROUP BY 1'''))
r = r.all()
for row in r:
    print(row)
print('querry3')
r = conn.execute(text('''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*) FROM table_name GROUP BY 1, 2'''))
r = r.all()
for row in r:
    print(row)
print('querry4')
r = conn.execute(text('''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*) FROM table_name GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC'''))
r = r.all()
for row in r:
    print(row)
"""
