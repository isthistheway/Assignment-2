class Pizza:
    def __init__(self, name, price, toppings):
        self.name = name
        self.price = float(price)
        self.toppings = toppings

def parse_pizza_string(pizza_string):
    pizza_info = pizza_string.strip().split('$')
    name = pizza_info[0].strip()
    price = pizza_info[1].strip()
    toppings = [topping.strip() for topping in pizza_info[2].split(',')]
    return Pizza(name, price, toppings)

# Function to read the menu file and get a list of pizzas
def read_menu_file(file_path):
    with open(file_path, 'r') as file:
        menu_data = [line.strip() for line in file.readlines()]
    return menu_data

# Usage example:
if __name__ == "__main__":
    menu_file = "menu.txt"
    menu_data = read_menu_file(menu_file)

    # Parsing the menu data and creating Pizza objects
    pizza_menu = [parse_pizza_string(pizza_string) for pizza_string in menu_data]

    # Printing the parsed pizzas
    for pizza in pizza_menu:
        print(f"{pizza.name} - ${pizza.price:.2f}")
        print("Toppings:")
        for topping in pizza.toppings:
            print(topping)
        print()
