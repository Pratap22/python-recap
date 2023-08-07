# # Functions
# # In programming, a function is a reusable block of code that
# # executes a certain functionality when it is called

# # Types of function
# # 1. Standard library functions
# # 2. User-defined functions

# # def function_name():
# #     # body
# #     print("Learn With Pratap")

# # function_name()

# # def sum():
# #     a = 10
# #     b = 11

# #     print("Sum of two numbers is ", a + b)

# # sum()

# def add_numbers(num1, num2=20):
#     print(num1, num2)
#     sum = num1 + num2
#     print("Sum is ", sum)

# add_numbers(19)

def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum


total = add_numbers(19, 20)
print(total)


def find_square(num):
    return num * num


my_numbers = [1, 2, 3, 4]

sqaure_of_numbers = [find_square(num) for num in my_numbers]

print(sqaure_of_numbers)

# benifits
# 1. COde reuseable
# 2. code readability