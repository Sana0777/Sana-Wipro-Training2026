import re

text="This is my email address admin123@gmail.com and another is admin@gmail.com"
pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
result=re.search(pattern,text)
if result:
    print("first occurrence of email in text is found ::",result.group())
else:
    print("no valid email found in text")