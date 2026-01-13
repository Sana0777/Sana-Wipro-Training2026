##	3. Create a dictionary comprehension where the key is the number and the value is its cube

data = [1, 2, 3, 4, 5, 6, 2, 4]
cube_dict={}
for i in data:
    cube_dict[i]=i**3
print(cube_dict)