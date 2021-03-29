from itertools import product, combinations, permutations, dropwhile, count, \
    cycle, repeat, accumulate, chain, compress, groupby, islice, takewhile, zip_longest

# Infinite Loops

for i in count(1, 11):
    print(i)
    if i % 100 == 0:
        break

cnt = 0
for i in cycle('ABCD'):
    cnt += 1
    print(i)
    if cnt == 100:
        break

# Iterators terminating on the shortest input sequence

res = accumulate([1, 2, 3, 4, 5], lambda x, y: x + 1.05 * y)
print(f'Acumulate :- {list(res)} ')

res = chain('abc', 'xyz')
print(f'Chain - {list(res)}')

res = chain.from_iterable(['abc', 'xyz'])
print(f'chain.from_iterables - {list(res)}')

# res = compress('abcdefgh', [0, 1, 0, 0])
res = compress('abcdef', [1, 1, 0, 1])
print(f"Compress - {''.join(list(res))}")

"""
Drop all the elements as long as condition function is satisfied. Post that it will not check & give everything.
 
"""
x = dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])
print(f'DropWhile {list(x)}')

# Group by Example in List of Dictionary
my_dict = [{'name': 'Bibash', 'class': 10}, {'name': 'Indu', 'class': 9}, {'name': 'Sharmi', 'class': 9}]

x = groupby(my_dict, key=lambda x: x['class'])

for k, g in x:
    print(f'key={k} ')
    for name in g:
        print(f'GroupBy on ListOfDicts - {" " * 5}{name["name"]}')

# Group by Example in List of Strings for grouping based on First character.

my_list = ["Indu", "Indira", "Bibash", "Bib", "Bisitha", "Sharmi", "Sharmila"]

x = groupby(my_list, key=lambda x: x[0])
for k, g in x:
    print(f'Count of words Starting with {k} ===> {(k, len(list(g)))}')

# Group by Example  of a String :: This helps in compressing consecutive duplicates.
x = groupby("AACCEDDA")
for k, g in x:
    print(f'{(k, len(list(g)))}', end=' ')
# Gives Output : ('A', 2) ('C', 2) ('E', 1) ('D', 2) ('A', 1)


"""
islice is used for slicing the Generator - Iterators. Dictionary/Set/Tuple Comprehensions & 
/map/Filter/dict object
Example - Slicing on Map object  will Fail. 
"""

x = map(str, [1, 2, 3, 4, 5])
try:
    print(x[1:3])  # Fail
except TypeError as e:
    print(f'\nSlicing in Generators : {list(islice(x, 1, 3))}')  # Pass

"""
Take while the condition is met. 
"""

x = takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])
print(f'takeWhile {list(x)}')  # Outputs - [6,4,1]

"""
zip_longest considers the Longest List and if there is no value in shorter list, it assigns None. 

"""
a = [1, 2, 3]
b = ['x', 'y']
print(list(zip_longest(a, b)))  # [(1, 'x'), (2, 'y'), (3, None)]
print(list(zip(a, b)))  # [(1, 'x'), (2, 'y')]


pr = product('ABCD', repeat=3) # n^r 
p = permutations('ABCD', 3) # n!/(n-r)!
c = combinations('ABCD', 3) # n!/r!(n-r)!
print(f'{len(list(pr))} \n {list(p)} \n  {list(c)}')
