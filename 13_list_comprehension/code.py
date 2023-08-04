# List comprehension
# List comprehension offers a shorter syntax 
# when you want to create a new list based on the values of an existing list.

my_list = [1,2,3,4,5,6,7,8,9,10]

odd = []
for number in my_list:
    if number % 2 != 0:
        odd.append(number)

odd_shorter = [number for number in my_list if number % 2 != 0]

# print("Odd numbers", odd)
# print("Odd numbers Shorter", odd_shorter)

def is_odd(num):
    return num % 2 != 0

a = [num for num in my_list if is_odd(num)]
b = [num for num in my_list if (lambda x: x%2 != 0)(num)]

print("List comprehension using function in condition", a)