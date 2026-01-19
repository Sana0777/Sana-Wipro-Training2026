class Addition:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value+other.value

obj1=Addition(20)
obj2=Addition(30)

print(obj1+obj2)