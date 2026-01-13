##2. Uses filter() with a lambda to select only even numbers

n=[1,7,8,5,3,9,10,15,12,14]
even_num=list(filter(lambda x:x%2==0,n))
print(even_num)