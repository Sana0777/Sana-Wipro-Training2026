def add(a,b):
    print(a+b)

add(10,20)

def sub(a,b):
    return a-b
print(sub(100,20))

def hello(greeting='Hello',name='World'):
    print('%s %s' % (greeting,name))
hello()

def print_params(*param):
    print(param)
print_params(10,20,30,40)
print_params("testing")

def print_params1(**param):
    print(param)
print_params1(x=10,y=20,z=30)