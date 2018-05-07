""" NamedTuples are immutable objects like tuple, namedtuple created the immutable class dynamically."""

from collections import namedtuple
import random

Cards = namedtuple('Cards', 'suit rank')

# Above creates an immutable Class named Cards, which has two properties and following methods.
# Lets apply them one-by-one

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
