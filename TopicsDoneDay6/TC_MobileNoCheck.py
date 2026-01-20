mobileNo=input("Enter mobile number : ")
result=re.fullmatch(r"\d{10}",mobileNo)
if result:
    print("valid mobile number",result.group())
else:
    print("Invalid mobile number")