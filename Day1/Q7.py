##2. Create a set comprehension to store only unique even numbers

data = [1, 2, 3, 4, 5, 6, 2, 4]

##approach1

even_num=set(filter(lambda x:x%2==0,data))
print(even_num)


##approach2
s1=set()
for i in data:
    if(i%2==0):
        s1.add(i)
print(s1)