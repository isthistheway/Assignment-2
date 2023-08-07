eachLine = "Margarita Pizza $12 tomato sauce, mozzarella cheese, cheddar cheese"

name_and_price = eachLine[1].split()
name = name_and_price[0]
price = float(name_and_price[1])
toppings = name_and_price[2:]