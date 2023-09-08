open_menu = open("menu.txt", "r")
        # opens the menu.txt file for reading and all the text file contents
        # a list of strings
lines = open_menu.readlines()        

pizza_info_separated = []
for eachLine in lines:
    eachLine = eachLine.strip()
    pizza_info = eachLine.split(' $')
    name = pizza_info[0]
    string_price = pizza_info[1][:2]
    price = float(string_price)
    toppings = pizza_info[1][3:].split(", ")

    formatted_toppings = ", ".join(toppings)
print(formatted_toppings)

