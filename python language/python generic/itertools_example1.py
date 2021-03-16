from itertools import groupby, ifilter


data_list = [{"Bytes": 10, "city": "Baglung", "Country": "Nepal", "ip": "10.1.0.20"},
             {"Bytes": 10, "city": "Delhi", "Country": "India", "ip": "20.1.0.20"},
             {"Bytes": 20, "city": "Bangalore", "Country": "India", "ip": "20.1.0.21"},
             {"Bytes": 30, "city": "Baglung", "Country": "Nepal", "ip": "10.1.0.21"}]*100000


# Apply GroupBy Fields & Sum of Bytes

agg_filed = 'Bytes'

groupby_fields =['Country','city']

transofromed_sum = ( {agg_filed: sum (x[agg_filed] for x in group) } for key, group in
                groupby (sorted(data_list, key=lambda x: [x[p] for p in groupby_fields]), key=lambda x: [x[p] for p in groupby_fields] ))



# Apply Filter on Bytes > 10

filtered = ifilter(lambda x : [x["Bytes"] > 20 ], data_list)
print list(filtered)[0]

N= 10

print list(transofromed_sum)[:N]
