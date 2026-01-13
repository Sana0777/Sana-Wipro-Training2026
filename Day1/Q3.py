##3. Uses map() with a lambda to square the filtered numbers

n=[1,7,8,5,3,9,10,15,12,14]
square_num=list(map(lambda x:x*x,n))
print(square_num)