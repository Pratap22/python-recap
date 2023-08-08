# Python *args and **kwargs
# *args: Unpacking arguments
# **kwargs: Unpacking keyword arguments

def adder(*args):
    print("Data type of *args is ", type(args))
    sum = 0
    for num in args:
        sum = sum + num

    print(sum)
    

adder(10,11,12,13)
adder(10)
adder(10, 12)

def introduction(**kwargs):
    print("Data type of **kwargs is ", type(kwargs))

    for key, value in kwargs.items():
        print(f"{key} is {value}")



introduction(name="Pratap", age="25", address="Nepal")
introduction(name="Madhav", age="30", address="Bangladesh")

# Things to Remember:

# *args and **kwargs are special keyword which allows function to take variable length argument.
# *args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed.
# **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
# *args and **kwargs make the function flexible.