numbers=[2,4,7,4,9]
names=["Sana","Shifa","Shalaj","Shamiya"]
mixed=[1,"Hari",3.12]
print(numbers)
print(names)
print(mixed)

numbers[1]=100

for i in numbers:
    print(i)

if 4 in numbers:
    print("found")

matrix=[[1,2,3],[4,5,6]]
print(matrix[1][2])

names.reverse()
print(names)

names.append("Aayat")
print(names)

names.extend(["Aayara","Anu"])
print(names)

names.remove("Aayara")
print(names)

names.insert(3,"Uma")
print(names)