from datetime import date

# class Calculator:

#     def __init__(self, version):
#         self.version = version
    
#     def description(self):
#         print(f"Currently the version of calculator is : {self.version}")

#     @staticmethod
#     def add_numbers(*numbers):
#         return sum(numbers)


# calc1 = Calculator(10)
# calc2 = Calculator(100)

# calc1.description()
# calc2.description()

# print(Calculator.add_numbers(10,11,12))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} is {self.age} years old")

    @classmethod
    def age_from_year(cls, name, birth_year):
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)
    

pratap = Person("Pratap", 20)
pratap.description()

madhav = Person.age_from_year("Madhav", 1990)
madhav.description()