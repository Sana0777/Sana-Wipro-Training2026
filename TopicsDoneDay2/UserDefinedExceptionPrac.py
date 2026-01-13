class invalideAge(Exception):
    pass


try:
    age=int(input("Enter your age : "))
    if age<18:
        raise invalideAge("Age must be 18 or above")
    else:
        print("eligible to vote")
except invalideAge as e:
    print("Error:",e)