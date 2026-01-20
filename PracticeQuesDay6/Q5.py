import re

def password_Check(password):
    pattern = r"""
    ^(?=.*[A-Z])
    (?=.*[a-z])
    (?=.*\d)
    (?=.*[@$!%*?&])
    .{8,}
    $"""
    return bool(re.match(pattern, password,re.VERBOSE))

password = input("Enter password: ")

if password_Check(password):
    print("Strong password")
else:
    print("Weak password")


