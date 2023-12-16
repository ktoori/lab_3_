import psycopg2
import time

def q_psycopg2(q, k):
    start = time.time()
    for i in range(10):
        cursor.execute(q)
        res = cursor.fetchall()
    end = time.time()
    print("The time Q", k, "is :", (end - start)/10, "s")

Q = ['''SELECT "VendorID", COUNT(*) FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", AVG("total_amount")FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*) FROM table_name GROUP BY 1, 2''',
     '''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*) 
     FROM table_name GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;''']

conn = psycopg2.connect('postgresql://postgres:postgres@localhost:5432/postgres')
cursor = conn.cursor()

q_psycopg2(Q[0], 1)
q_psycopg2(Q[1], 2)
q_psycopg2(Q[2], 3)
q_psycopg2(Q[3], 4)

cursor.close()
conn.close()

