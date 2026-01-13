try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Division by zero")
try:
    n=int(input("enter a number"))
    print(10/n)
except ValueError:
    print("invalid entery")

except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("Excecution is successull")