import datetime

# __init__
# __str__
# __repr__

# my_date = datetime.datetime.now()

# print("__str__() string: ", my_date.__str__())
# print("str() string: ", str(my_date))

# print("__repr__() string: ", my_date.__repr__())
# print("repr() string: ", repr(my_date))


class Room:
    length = 0
    breadth = 0

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __str__(self):
        return f"The length is {self.length} and the breadth is {self.breadth}"
    
    def __repr__(self):
        return f"Room({self.length},{self.breadth})"

dinning_room = Room(100, 80)

print(str(dinning_room))
print(repr(dinning_room))

kitchen = eval(repr(dinning_room))

print(kitchen)
