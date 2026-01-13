##2. Uses filter() with a lambda to select only even numbers
data = [1, 2, 3, 4, 5, 6, 2, 4]

even_numbers = list(filter(lambda x: x % 2 == 0, data))

print(even_numbers)
