"""
Find the missing number from 1 to 100.
Sum = n * (n+1)/2
"""

my_list = list(range(1,101))
my_list.remove(50) 
n = 100
expected_sum = n*(n+1)//2
missing = expected_sum - sum(my_list)
print(f'Missing Number : {missing}')
