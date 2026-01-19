class animal:
    def sound(self):
        print("Animals makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class cat(animal):
    def sound(self):
        print("cat meows")

obj=[dog(),cat()]
for i in obj:
    i.sound()