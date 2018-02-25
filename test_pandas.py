from __future__ import print_function
import pandas as pd
from datetime import datetime

data_list = [{"@timestamp":1514833348.1, "Bytes": 10, "city": "Baglung", "Country": "Nepal", "ip": "10.1.0.20"},
            {"@timestamp":1514833148.1,"Bytes": 20, "city": "Baglung", "Country": "Nepal", "ip": "10.1.0.20"},
             {"@timestamp":1514833448.1,"Bytes": 10, "city": "Delhi", "Country": "India", "ip": "20.1.0.20"},
             {"@timestamp":1514833548.1,"Bytes": 20, "city": "Bangalore", "Country": "India", "ip": "20.1.0.21"},
             {"@timestamp":1514833648.1,"Bytes": 30, "city": "Baglung", "Country": "Nepal", "ip": "10.1.0.21"}]*1000000

# Group by one or more Multiple Conditions

def index_sort(data_list):
    df = pd.DataFrame (data_list)
    df['@timestamp'] = pd.to_datetime (df['@timestamp']*1000, unit='ms', errors='coerce')
    df = df.set_index ("@timestamp")
    df = df.sort_index()
    return df

def groupby_sum(df, groupbyfields, aggregates, N):
    df = df.groupby(groupbyfields.split(',')).agg(aggregates).sum().reset_index(drop=False)
    df = df.sort_values(by=aggregates)
    return df.head(N)

def filter(df, conditions,N):
    df = df.query (conditions, inplace=False)
    return df.head(N)

df = index_sort(data_list)

#Testing ....!

groupbyfields="Country,city"
conditions = "Bytes > 20 and city == 'Baglung'"
aggregates = "Bytes"

N = 100

t1 = datetime.now()

print("GroupBy: {} and SUM of: {}\n".format(groupbyfields, aggregates))
print(groupby_sum (df, groupbyfields, aggregates, N))

t2 = datetime.now()

print("Filter on Condition:  {}\n".format(conditions))
print (filter (df, conditions, N))

t3 = datetime.now()

print ("groupBy & Sum , Time taken: {}\n".format (t2 - t1))
print("Filter , Time taken: {}\n".format (t3 - t2))
