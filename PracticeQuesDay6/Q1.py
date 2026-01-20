import re
empid=input("enter employee id::")
pattern=r"^EMP\d{3}"
result=re.match(pattern,empid)
if result:
    print("Valid Employee ID",result.group())
else:
    print("Invalid Employee ID")


##  ^ -->start of the string
##  EMP-->literal characters
##  \d{3}-->Exactly 3 digits(0-9)