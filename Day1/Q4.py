##4. Uses reduce() to calculate the sum of squared even numbers

from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9]

result=reduce(lambda x,y:x+y,map(lambda x:x*x,filter(lambda x:x%2==0,numbers)),0)
print(result)
