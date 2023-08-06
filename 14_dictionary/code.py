my_dict = {"name": "Pratap", "age": 28, "address": "Nepal",
           1: "One", (1, 2): "This is tuple"}

# print(my_dict)

my_dict_2 = dict({"name": "Pratap", "age": "25"})

# print(my_dict["name"])
my_dict["address"] = "Pokhara"
my_dict.update({"gender": "Male"})
# my_dict.clear()
# print(my_dict)

for key, value in my_dict.items():
    print(key, value)