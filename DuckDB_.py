import duckdb
import time

def q_duck(q, k):
    start = time.time()
    for i in range(10):
        c.sql(q)
        #c.sql(q).show для вывода результата sql запроса
    end = time.time()
    print("The time Q", k, "is :", (end - start)/10, "s")

Q = ['''SELECT "VendorID", COUNT(*) FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", AVG("total_amount")FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*) FROM table_name GROUP BY 1, 2''',
     '''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*) 
     FROM table_name GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;''']

conn = duckdb.connect('myduckdb.duckdb')
c = conn.cursor()
c.execute("CREATE TABLE table_name AS SELECT * FROM read_csv_auto('nyc_yellow_tiny.csv')") #При повторном запуске данную строчку закомментить, т.к. таблица уже создана

q_duck(Q[0], 1)
q_duck(Q[1], 2)
q_duck(Q[2], 3)
q_duck(Q[3], 4)

c.close()
conn.close()
