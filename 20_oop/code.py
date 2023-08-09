# Python Object Oriented Programming
# classes and objects

# parrot - object
# attributes - name, age, color
# behaviour - fly, sing, etc

# A class is a blueprint

# class ClassName:
#     # class defination

class Bike:
    name = ""
    gear = 0

pulsar = Bike()
yamaha = Bike()
tvs = Bike()
unicorn = Bike()


pulsar.name = "Pulsar 180"
pulsar.gear = 4

# print(pulsar.name)
# print(pulsar.gear)

class Room:
    length = 0
    breadth = 0

    def calculate_area(self):
        print(self.length)
        print(self.breadth)
        print(f"Area of room = {self.length * self.breadth}")

dinning_room = Room()
dinning_room.length = 100
dinning_room.breadth = 80

# dinning_room.calculate_area()

class Human:
    name = ""
    age = 0

    # dunder method
    # constructor method
    def __init__(self, name, age):
        print(name, age)
        self.name = name
        self.age = age

pratap = Human("Pratap", 20)