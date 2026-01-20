import re
text="apple banana apple mango apple"
pattern=input("Enter pattern you want check::")
result=re.finditer(pattern,text)
found=False
for match in result:
    found=True
    print(match.group(),match.start(),match.end())
if not found:
    print("Pattern not found")

