# User defined Exception

# class CustomError(Exception):
#     pass

# try:
#     ...
# except CustomError:
#     ...

# class InvalidAgeException(Exception):
#    pass

class InvalidAgeException(Exception):
    
    def __init__(self, age, message="You must be 18 years and above"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# try:
#     user_age = int(input("How old are you? "))
#     if user_age < 18:
#         raise InvalidAgeException
#     else:
#         print("You are permitted to do some works")
# except InvalidAgeException:
#     print("Exception occured: Invalid Age")


user_age = int(input("How old are you? "))
if user_age < 18:
    raise InvalidAgeException(user_age)
else:
    print("You are permitted to do some works")