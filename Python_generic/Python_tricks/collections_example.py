
from collections import namedtuple, Counter, ChainMap, OrderDict, defaultdict  
import random

""" 
NamedTuples are immutable objects like tuple, namedtuple created the immutable class dynamically
Below creates an immutable Class named Cards, which has two properties and methods.
Lets apply them one-by-one.

"""

Cards = namedtuple('Cards', 'suit rank')


print(type(Cards('Heart', '1')))  # The type is the instance of the Class Cards i.e <class '__main__.Cards'>
print(type(Cards))  # This prints the instance of 'Type' i.e <type 'type'>
# Extract the properties of Cards class.
print(Cards._fields)  # ('suit', 'rank')
# Lets use the Cards class to form the Deck of Cards.

my_cards = []
for suits in ['Heart', 'Spade', 'Diamond', 'Club']:
    # noinspection PyTypeChecker
    for rank in range(2, 11) + 'A J Q K'.split():
        my_cards.append(Cards(suits, rank))

random.shuffle(my_cards)

for i in my_cards:
    print(tuple(i))

    
"""
ChainMAP can be used as an alternative to dict.update only of you don't have same keys in two dictionaries.
Two Update the Values of Second Dictionary within ChainMap Use -> my_chain.maps[1]['c'] = 100
ChainMap changes are reflected in Original Dictionary . To Change Behaviour , Use new_child for temporary Modification.
That is possible because new_child method adds one extra empty map within the ChainMap.
"""
dict1  = {'d':1, 'b':2 }
dict2  = {'c':1, 'a': 20 }
my_chain = ChainMap(dict1, dict2)
my_chain1 = my_chain.new_child()
my_chain1.maps[2]['c'] = 100
print("Original Second", dict2)
print(my_chain1)

"""
Counter - Example 1

"""

my_input = {'a':2, 'b':3}
c = Counter(my_input)
print(c) # Gives the Dictionary of counters
print(c.most_common(2))
print(list(c.elements()))  # Converts from Dictionary to exapanded List. 

"""
Counter - Example 2 : Most frequent words in a file with Counter.
Output looks like : 
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554), ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
 
"""

words = re.findall(r'\w+', open('hamlet.txt').read().lower())
c = Counter(words).most_common(10)
print(c)


from collections import OrderedDict

"""
Let's Say you are Given a Input String with all upper letter. Divide the Strings by k  and 
in each parts , remove the duplicates but maintain the order.

Example - String = AADCBHDDDACD  & k = 3 . Output should be : ADC BHD DAC

"""
string = 'AADCBHDDDACD'
n = len(string)
k = 4
for i in range(0, n, k):
    part_string = string[i:i+k]
    # Order dictionary is not needed here if you are using Py-3.6+ 
    res = list(OrderedDict.fromkeys(string[i:i+k])) 
    print(''.join(res))

"""
Default Dictionary assigns the default value to keys which doesn't exist. 
In following example, 1 not  is in dict x for the first time but it doesnt throw key error. Instead pass the default 100. 
"""
a = [1, 2, 2, 1, 1, 0]
x = defaultdict(lambda: 100)
for i in a:
    x[i] = x[i] + 1
print(dict(x))

"""
Default Dictionary assigns the default List to keys which doesn't exist. 
In following example, 1 not  is in dict x for the first time but it doesnt throw key error. Instead pass the default [] list and keep appending. 
"""
a = [1, 2, 2, 1, 1, 0]
x = defaultdict(list)
for i in a:
    x[i].append(i)
print(dict(x))

