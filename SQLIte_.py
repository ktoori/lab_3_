import sqlite3
import time

def q_SQLite(q, k):
    start = time.time()
    for i in range(10):
        cursor.execute(q)
    end = time.time()
    print("The time Q", k, "is :", (end - start), "s")

Q = ['''SELECT "VendorID", COUNT(*) FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", AVG("total_amount")FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", strftime('%Y', "tpep_pickup_datetime"), COUNT(*) FROM table_name GROUP BY 1, 2;''',
     '''SELECT "passenger_count", strftime('%Y', "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*) 
     FROM table_name GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;''']

db_file = 'C:\\Users\\crugv\\lab_3\\mydb.db'
conn = sqlite3.connect(db_file)
#tiny = 'nyc_yellow_tiny.csv'
#df = pd.read_csv(tiny)
#if 'Airport_fee' in df:
#    df.pop('Airport_fee')
#df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
#df.to_sql('table_name', conn, if_exists = 'replace', index = False)
cursor = conn.cursor()

q_SQLite(Q[0], 1)
q_SQLite(Q[1], 2)
q_SQLite(Q[2], 3)
q_SQLite(Q[3], 4)

cursor.close()
conn.close()
