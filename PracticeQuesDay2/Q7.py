##2. Create a set comprehension to store only unique even numbers

data = [1, 2, 3, 4, 5, 6, 2, 4]

unique_even_numbers = {x for x in data if x % 2 == 0}

print(unique_even_numbers)
