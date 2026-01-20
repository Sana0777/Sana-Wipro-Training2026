import re

text = "Hello World 123 color colour aab ab abb"

print("Dot :", re.findall(r"a.b", text))

print("Asterisk :", re.findall(r"ab*", text))

print("Plus :", re.findall(r"ab+", text))

print("Colo?r :", re.findall(r"colou?r", text))

print("Digits :", re.findall(r"\d+", text))

print("Word characters :", re.findall(r"\w+", text))

print("Whitespace:", re.findall(r"\s", text))
