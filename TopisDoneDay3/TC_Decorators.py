def mydecorator(sayhello):
    def wrapper():
        print("Before Function Call")
        sayhello()
        print("After Function Call")

    return wrapper

@mydecorator
def sayhello():
    print("Hello")
sayhello()