class animal:
    def speak(self):
        print("Animal makes sound")

class dog(animal):
    def bark(self):
        print("Dog barks")

obj1=dog()
obj1.speak()
obj1.bark()