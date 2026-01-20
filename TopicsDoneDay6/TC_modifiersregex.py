import re
print(re.search("python","Python",re.I))

text4="one\ntwo\nthree"
print(re.findall(r"^t\w+",text4,re.M))