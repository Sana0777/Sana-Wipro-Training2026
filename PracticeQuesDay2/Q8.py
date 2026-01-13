##3. Create a dictionary comprehension where the key is the number and the value is its cube
data = [1, 2, 3, 4, 5, 6, 2, 4]

number_cubes = {x: x ** 3 for x in data}

print(number_cubes)
