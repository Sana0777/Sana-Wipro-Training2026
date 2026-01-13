##3. Uses map() with a lambda to square the filtered numbers

data = [1, 2, 3, 4, 5, 6, 2, 4]

squared_even_numbers = list(
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, data))
)

print(squared_even_numbers)
