class Calculator:
    def add(self):
        pass
    def multiply(self):
        pass

class AdvanceCalculator(Calculator):
    def add(self,a,b,c=0):
        print("advanced addition: ",a+b+c)
    def multiply(self,a,b,c=0):
        print("advanced multiplication: ",a*b*c)
obj = AdvanceCalculator()
obj.add(2,3)
obj.add(2,3,4)
obj.multiply(2,3,4)
