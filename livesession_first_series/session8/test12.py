#!/usr/bin/python3

"""
Problem: 
Give a list of list as: 
mylist = [ ['vivek','math',100], ['Ashok','math',200],['Vinod','math',150],['vivek','math',10], ['mayuri','math',300] ]
Aggregate the score for each names in the nested list & print top kth scorer 
i.e. Output - Mayuri - 300, Ashok - 200, Vinod-150 

"""
mylist = [['vivek', 'math', 100], ['Ashok', 'math', 200], [
    'Vinod', 'math', 150], ['vivek', 'math', 10], ['mayuri', 'math', 300]]

result = {}
for sublist in mylist:
    key = sublist[0]
    value = sublist[2]
    if key not in result:
        result[key] = value
    else:
        result[key] = result[key] + value

# upto kth scorer
k = 3
print(f'Top {k} scorers are:')
for k, v in sorted(result.items(), reverse=True, key=lambda x: x[1])[0:k]:
    print(f'{k} - {v} ', end=',')
