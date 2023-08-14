# Python First Class function

# def double(num):
#     return num * 2

# my_double = double
# print(my_double(5))
# print(double(5))

# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# # Higher Order Function
# def greet(func):
#     greeting = func("Hi There")
#     print(greeting)

# greet(whisper)

# Higher Order FUnctio
def first_child():
    return "Hi, I am Pratap"

def second_child():
    return "Hi, I am Madhav"

def parent(num):
    if num == 1:
        return first_child
    else:
        return second_child
    
my_parent = parent(1)
print(my_parent)
print(my_parent())