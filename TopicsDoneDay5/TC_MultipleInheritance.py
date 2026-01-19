class A:
    def showA(self):
        print("I am A")
class B:
    def showB(self):
        print("I am B")
    def showA(self):
        print("I am method showA implemented again in B")

class C(B,A):
    def showC(self):
        print("I am C")

obj=C()
obj.showC()
obj.showB()
obj.showA()