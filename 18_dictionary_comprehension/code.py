square_dict = dict()

for num in range(1,11):
    square_dict[num] = num*num

# print(square_dict)

square_dict_com = {num: num * num for num in range(1,11)}
# print(square_dict_com)

# {var: var * var for var in iterable}

# print({num: "Pratap" for num in range(1,11)})

# price is in dollar
old_price = {'milk': 1.02, 'veg': 2.5, 'spinach': 3}

dollar_to_npr = 131

new_price = {item: value * dollar_to_npr for (item, value) in old_price.items()}

print(new_price)

#davantages
# It shortens our code
# It makes our code pythonic