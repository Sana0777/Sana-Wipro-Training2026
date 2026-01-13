##4. Uses reduce() to calculate the sum of squared even numbers

from functools import reduce

data = [1, 2, 3, 4, 5, 6, 2, 4]

sum_of_squared_even_numbers = reduce(
    lambda a, b: a + b,map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, data))
)

print(sum_of_squared_even_numbers)

