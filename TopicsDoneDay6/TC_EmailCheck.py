import re

email="admin123@gmail.com"
if(re.match(r"[a-zA-Z0-9._]+@",email)):
    print(" Valid email address")
else:
    print("Enter valid email address")


