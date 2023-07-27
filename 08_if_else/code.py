# Equals a = b
# Not Equals: a != b
#less than: a < b
# less than or equal: a <=b
# greater than: b > c
# greater than or equal: b >= c

a = 11
b = 10
if a < b:
    print("A is less than B")
elif a == b:
    print("Both numbers are equal")
elif a+ 1 == 5:
    print("Addition of 1 in A equals B")
else:
    print("A is greater than B")

#short hand if
if a > b: print("a is greater than b")

#short hand if..else
print("A") if a > b else print("B")

if not a > b:
    print("A is not greater than B")
else:
    print("A is greater than B")