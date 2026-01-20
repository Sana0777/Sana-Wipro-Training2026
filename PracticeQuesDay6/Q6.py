import re
text = "Hello\nWORLD\nPython123"

print(re.findall(r"world", text, re.IGNORECASE))
print(re.findall(r"^Hello", text, re.MULTILINE))
print(re.findall(r"Hello.*123", text, re.DOTALL))