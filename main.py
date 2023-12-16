import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
tiny = 'nyc_yellow_tiny.csv'
df = pd.read_csv(tiny)
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df.to_sql('table_name', engine, if_exists='replace', index=False)
