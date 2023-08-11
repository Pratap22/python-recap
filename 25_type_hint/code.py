#
# Type Hints - Learn With Pratap
#

def greet(name: str) -> str:
    return "Hello, " + name

# print(greet("Learn With Pratap"))

def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")

print(headline("Learn With Pratap"))
print(headline("Learn With Pratap", False))


# In terms of style, PEP 8 recommends the following:

# 1. Use normal rules for colons, that is, no space before and one space after a colon (text: str).
# 2. Use spaces around the = sign when combining an argument annotation with a 
# default value (align: bool = True).
# 3. Use spaces around the -> arrow (def headline(...) -> str).