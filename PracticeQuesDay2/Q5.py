##5. Uses enumerate() to print the index and value of the final result list

from functools import reduce

data = [1, 2, 3, 4, 5, 6, 2, 4]
for index, value in enumerate(data):
    print(index, value)
