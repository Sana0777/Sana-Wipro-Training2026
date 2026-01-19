class parent:
    def parent1(self):
        print("parent1")

class child1(parent):
    def c1(self):
        print("child1")

class child2(parent):
    def c2(self):
        print("child2")

obj1 = child1()
obj1.c1()
obj1.parent1()

obj2 = child2()
obj2.c2()
obj2.parent1()

