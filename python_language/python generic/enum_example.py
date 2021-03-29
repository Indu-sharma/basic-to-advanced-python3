from enum import Enum, unique, IntEnum


@unique  # To Avoid duplicate Aliases
class Color(Enum):
    RED = '1'
    GREEN = 2
    BLUE = 3


x = Color.RED.value  # Capture Value by  Key
y = Color(2).name  # Capture Key by Value

print(x, y)

for i in Color:
    print(i.name, i.value)


@unique  # To Avoid duplicate Aliases & IntEnum makes sure you have only Integers
class Color(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3


x = Color.RED.value  # Capture Value by  Key
y = Color(2).name  # Capture Key by Value
print(x, y)
