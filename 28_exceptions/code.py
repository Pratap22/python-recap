# Python Exceptions

num_1 = 7
num_2 = 0

my_list = [1,2]

try:
    print(num_1/num_2)
    print(my_list[2])
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print("I cannot divide", e)
except Exception as e:
    print(e)
else:
    print("I am else")
finally:
    print("I am finally")

print("Learn with Pratap")