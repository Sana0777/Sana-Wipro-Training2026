class greeting:
    def greet(self):
        print("There are different types of greetings in each language")
class InEnglish(greeting):
    def greet(self):
        print("In English--hello")
class InSpanish(greeting):
    def greet(self):
        print("In Spanish--Hola")
class InHindi(greeting):
    def greet(self):
        print("In hindi--Namaste")

obj=[greeting(),InEnglish(),InSpanish(),InHindi()]
for i in obj:
    i.greet()