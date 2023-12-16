import pandas as pd
from sqlalchemy import create_engine
import time

def q_Pandas(q, k):
    start = time.time()
    for i in range(10):
        pd.read_sql(q, con=engine)
    end = time.time()
    print("The time Q", k, "is :", (end - start) / 10, "s")

Q = ['''SELECT "VendorID", COUNT(*) FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", AVG("total_amount")FROM table_name GROUP BY 1;''',
     '''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*) FROM table_name GROUP BY 1, 2''',
     '''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*) 
     FROM table_name GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;''']

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
q_Pandas(Q[0], 1)
q_Pandas(Q[1], 2)
q_Pandas(Q[2], 3)
q_Pandas(Q[3], 4)

