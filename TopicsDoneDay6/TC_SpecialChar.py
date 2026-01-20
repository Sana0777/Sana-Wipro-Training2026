import re
from tokenize import group

print(re.search(r"\d+","Age is 25"))

print(re.search(r"^a.*c$","abnkkkkkknnc"))

m=re.search(r"\w+(?=@)","test@gmail.com")
print(m.group())

