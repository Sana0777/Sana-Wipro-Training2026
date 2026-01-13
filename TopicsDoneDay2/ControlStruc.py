num=24
if(num%2==0):
    print("number is even")
else:
    print("number is odd")

marks=87
if(marks>=90):
    print("grade A")
elif(marks>=80):
    print("grade B")
else:
    print("grade C")

for i in range(1,6):
    print(i)
j=1
while(j>=5):
    print(j)
    j=j+1

Day=int(input("enter your day "))
match Day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
