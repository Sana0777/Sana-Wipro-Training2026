import re
text="python is powerfull"
result=re.search(input("Enter the text you want to check::"),text)
if result:
    print("Match Found-->",result.group())
    print(result.start())
    print(result.end())
else:
    print(" Match not found")

## re.search() searches the entire string and returns the first occurrence of the pattern
