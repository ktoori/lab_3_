import pandas as pd
import time

table = pd.read_csv('nyc_yellow_tiny.csv')
table['tpep_pickup_datetime'] = pd.to_datetime(table['tpep_pickup_datetime'])

start = time.time()
for i in range(10):
    table[['VendorID']].groupby('VendorID').size().reset_index(name='count')
end = time.time()
print("The time Q 1 is :", (end - start) / 10, "s")

start = time.time()
for i in range(10):
    table[['passenger_count', 'total_amount']].groupby('passenger_count').mean().reset_index()
end = time.time()
print("The time Q 2 is :", (end - start) / 10, "s")

start = time.time()
for i in range(10):
    selected_df = table.loc[:, ['passenger_count', 'tpep_pickup_datetime']]
    selected_df['year'] = pd.to_datetime(
        selected_df.pop('tpep_pickup_datetime'),
        format='%Y-%m-%d %H:%M:%S').dt.year
    grouped_df = selected_df.groupby(['passenger_count', 'year'])
    final_df = grouped_df.size().reset_index(name='counts')
end = time.time()
print("The time Q 3 is :", (end - start) / 10, "s")

start = time.time()
for i in range(10):
    selected_df = table.loc[:, ['passenger_count', 'tpep_pickup_datetime', 'trip_distance']]
    selected_df['trip_distance'] = selected_df['trip_distance'].round().astype(int)
    selected_df['year'] = pd.to_datetime(
        selected_df.pop('tpep_pickup_datetime'),
        format='%Y-%m-%d %H:%M:%S').dt.year
    grouped_df = selected_df.groupby(['passenger_count', 'year', 'trip_distance'])
    final_df = grouped_df.size().reset_index(name='counts')
    final_df2 = final_df.sort_values(['year', 'counts'], ascending=[True, False])
end = time.time()
print("The time Q 4 is :", (end - start) / 10, "s")
