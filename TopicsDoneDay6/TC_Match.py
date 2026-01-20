import re
text="python is powerfull"
result=re.match(input("Enter the text you want to check::"),text)
if result:
    print("Match Found",result.group())
    print(result.start())
    print(result.end())

else:
    print(" Match not found")

## match only tries to match the pattern at beginning of the string if pattern
## is not at the start it returns not found
