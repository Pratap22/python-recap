# Mutability in Python

# Mutable - Liable to Change
# Immutable - Not Liable to change

# string, int, float, tuples - Immutable

# list - Mutable

# a = 10

# b = a

# print(id(a))
# print(id(b))

# a = 13

# print(id(a))
# print(id(b))

# my_name = "Pratap"

# my_name = "Prttap"

# print(my_name)

# my_list = [1,2,3]
# print(my_list)
# print(id(my_list))

# my_list[0] = 10
# print(my_list)
# print(id(my_list))

my_tuple = (1,2)

my_tuple[1] = 5

print(my_tuple)
