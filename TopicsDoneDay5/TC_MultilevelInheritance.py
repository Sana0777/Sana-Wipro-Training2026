class A:
    def showA(self):
        print("I am A")
class B(A):
    def showB(self):
        print("I am B")

class C(B):
    def showC(self):
        print("I am C")

obj=C()
obj.showC()
obj.showB()
obj.showA()