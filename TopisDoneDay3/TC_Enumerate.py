fruits=['apple','orange','banana','grapes']
for index,value in enumerate(fruits):
    print(index,value)

from enum import Enum


class color(Enum):
    Red = 1
    Green = 2
    Blue = 3


print(color.Red.value)
print(color.Red.name)
