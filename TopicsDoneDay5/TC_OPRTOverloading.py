class box1:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value + other.value
    def __mul__(self,other):
        return self.value * other.value
    def __sub__(self,other):
        return self.value - other.value

obj1=box1(15)
obj2=box1(5)
print(obj1+obj2)
print(obj1*obj2)
print(obj1-obj2)

