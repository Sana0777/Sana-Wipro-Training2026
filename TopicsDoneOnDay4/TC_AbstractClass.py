from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def display(self):
        print("this is the display class in Shape class")

class rectangle(Shape):
    def area(self):
        print("implementation of abstract method area")
    def display(self):
        super().display()
        print("I am extending the display class here in rectangle")

obj=rectangle()
obj.area()
obj.display()

