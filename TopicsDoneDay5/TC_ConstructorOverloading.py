class P:
    def __init__(self,name,age=None):
        self.name = name
        self.age = age

p1=P("Sana")
P2=P("Shifa",20)
print(p1.__dict__) ## will return the output in dictionary
print(P2.__dict__)
