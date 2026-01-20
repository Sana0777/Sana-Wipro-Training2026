import re

text = "My email is user123@gmail.com and contact number is 9876543210"

# Regex with capturing groups
pattern = r"(\w+)@(\w+)\.(\w+)"

match = re.search(pattern, text)

if match:
    print("Full match:", match.group(0))
    print("Username:", match.group(1))
    print("Domain name:", match.group(2))
    print("Extension:", match.group(3))
