# File: pizza_shop.py 
# Author: Volodymyr Gordiienko
# Id: 45701
# Description: This is my Assignment of OOP in COMP1046
# This is my own work as defined by the Academic Integrity policy. 

import math

class Ingredient:
    def __init__(self, Cost, Name, formatPrice):  
        self.__Cost = Cost
        self.__Name = Name
        self.__formatPrice = formatPrice
        # initialising the pizza_shop variable for the 
        # Ingredient --> PizzaShop aggregation relationship
        self.__pizza_shop = None
    
    # aggregation relationship between Ingredient and PizzaBase
    # Ingredient --> PizzaBase
    def PizzaBase_aggregation(self, pizza_base):
        self.__pizza_base = pizza_base
    # getter method for self.__pizza_base
    def get_pizza_base(self):
        return self.__pizza_base
    # getter method for the private variable pizza_shop
    # for the Ingredient --> PizzaShop aggregation
    def get_pizza_shop(self):
        return self.__pizza_shop
    # getter method for private variable self.__Cost
    def getCost(self):
        return self.__Cost
    # getter method for private variable self.__name
    def getName(self):
        return self.__Name
    # getter method for private variable self.__formatPrice
    def getFormatPrice(self):
        return self.__formatPrice
    # clone method to return a copy of the ingredients used in a pizza or the additional
    # toppings selected by the customer
    def clone(self):
        cloned_ingredients = Ingredient(self.__Cost, self.__Name, self.__formatPrice)
        return cloned_ingredients
    # equals method to check whether other is equal to the given self argument and whether
    # self and other are the same type of variable
    def equals(self, other):
        if self == other and type(self) == type(other):
            return True
        else:
            return False
    # returns a string of the formatPrice starting with a $ sign and formatted
    # to 2 decimal places
    def displayFormatPrice(self):
        return f"${self.__formatPrice:.2f}"

class PizzaShop:
    # PizzaBase's attributes are defined in PizzaShop's init method for the 
    # PizzaBase --> PizzaShop composition relationship
    def __init__(self):
        
        # initialise an empty dictionary for ingredients
        self.ingredients = {}
        # PizzaBase --> PizzaShop composition relationship
        # an instance of PizzaBase is created in the init method
        self.pizzaBase = None
    # Ingredient --> PizzaShop aggregation relationship method
    def add_ingredient_PizzaShop_aggregation(self, Name, Cost, formatPrice):
        # association relationship (PizzaShop --> Ingredient)
        ingredient = Ingredient(Cost, Name, formatPrice)
        # adds an ingredient to the self.ingredients dictionary
        # using Name as a unique identifier parameter for each item 
        # in the dictionary
        self.ingredients[Name] = ingredient
    
    def add_ingredient_PizzaBase_aggregation(self, ingredient):
        self.ingredients[ingredient]
        ingredient.PizzaBase_aggregation(self)
    def load_menu(self):
        # load the ingredients first before the menu
        self.load_ingredients()
        # set open_menu to a variable
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
            pizza = Pizza(name, price, toppings)
        
            for topping in toppings:
                pizza.addTopping(topping)
        
            pizza_info_separated.append(pizza)
            # full_pizza = f"{name}, large, thin crust ${price:.2f}:\n {formatted_toppings}"
            # pizza_info_separated.append(full_pizza)
            pizza_info_separated.append(Pizza(name, price, toppings))
            
        return pizza_info_separated
    
    def load_ingredients(self):
        filename = "ingredients.txt"
        # open the ingredient.txt file for reading
        open_ingredients = open(filename, "r")
        # make the ingredient list an empty list
        ingredients = []
        # read every line of the text file and return it as a list of strings
        
        for eachLine in open_ingredients:
            lines = open_ingredients.readlines()

            # remove any blank space characters or extra spaces
            stripped_line = eachLine.strip()

            # split the line to separate the name and price by the dollar symbol - the name and price get put into a list 
            # with the split() function and can then be accessed with index positions and the $ sign is not included in 
            # the list
            split_and_stripped_line = stripped_line.split("$")
            if len(split_and_stripped_line) == 2:
                # set the ingredient name to the name
                name = split_and_stripped_line[0].strip()
                # set the ingredient price to the price
                price = float(split_and_stripped_line[1].strip())
                # checks to see if the line starts with the word base and if it does, 
                # it makes it a PizzaBase
                if len(name) >= 4 and name[:4].lower() == "base":
                    # PizzaBase --> PizzaShop composition relationship
                    ingredient = PizzaBase("large", name, price)
                else:        
                    # composition relationship between PizzaShop and Pizza
                    # Pizza --> PizzaShop
                    # an instance of the Pizza class is created within the PizzaShop
                    # class and is then appended to the ingredients list as a single list item
                    ## if the line doesn't start with the word base, it makes it a
                    ## Pizza object with the name and price
                    ingredient = Pizza(name, price)
                
                ingredients.append(ingredient)

                self.ingredients[name] = ingredient
        # close the ingredients.txt file
        open_ingredients.close()

        return ingredients

    def __str__(self):
        return f"Pizza Base: {self.name}, Price: ${self.price:.2f}"
    
class PizzaBase(Ingredient):
    def __init__(self, pizzaSize, baseType, Cost):
        super().__init__(Cost, baseType, "$" + str(Cost))
        self.__pizzaSize = pizzaSize
        self.__baseType = ["deep pan", "cheese crust", "thin crust"]

        if pizzaSize == "small":
            self.__pizzaSize = 10
        elif pizzaSize == "medium":
            self.__pizzaSize = 12
        elif pizzaSize == "large":
            self.__pizzaSize = 14

    def getPizzaSize(self):
        return self.__pizzaSize
   
    def calcCostPerSquareInch(self):
        cost = float(self.getCost())
        pizza_size = float(self.__pizzaSize)
        cost_per_square_inch = float((cost/3.14) * ((pizza_size/2)**2))
        return cost_per_square_inch
    
    def setSize(self, newSize):
        self.__pizzaSize = newSize

    def getBase(self):
        return self.__baseType
    
    def setBase(self, newBase):
        self.__baseType = newBase
    # clone method to return a copy of the pizza base
    # use cloned for test code
    def clone(self):
        cloned_pizza_base = PizzaBase(self.__pizzaSize, self.__baseType, Ingredient.getCost(self))
        return cloned_pizza_base
    
    def set_size_string(self, newSize):
        sizes = {
            "small": 10,
            "medium": 12, 
            "large": 14
        }
        # check if the given newSize argument is a valid pizza size according to the sizes dictionary
        if newSize in sizes:
            # if 'newSize' is found in the sizes dictionary, it assigns the string's corresponding 
            # integer value to the __pizzaSize attribute
            self.__pizzaSize = sizes[newSize]

    # equals method to check whether other's argument is equal tn self's argument and whether
    # self and other are the same type of variable
    def equals(self, other):
        if type(self) == type(other) and \
            self.getCost() == other.getCost() and \
            self.getName() == other.getName() and \
            self.getPizzaSize() == other.getPizzaSize():
            return True
        else:
            return False

    def __str__(self):
        return "PizzaBase" + self.getName() + " " + str(self.__pizzaSize)

class Pizza(PizzaBase):
    def __init__(self, name, price, toppings):
        super().__init__("large", "thin crust", 13.00)
        self.__price = price
        self.__name = name
        self.__toppings = []

    def getName(self):
        return self.__name
    # getter method for the private variable self.__price
    def getPrice(self):
        return self.__price
    
    def setTopping(self):
        self.__toppings = []

    def addTopping(self, topping):
        self.__toppings.append(topping)

    def removeToppings(self, topping):
        if topping in self.__toppings:
            self.__toppings.remove(topping)

    # getter method for the private variable self.__toppings
    def getToppings(self):
        return self.__toppings
    
    # clone method to create a copy of the pizza
    def clone(self):
        cloned_pizza = Pizza(self.price)
        return cloned_pizza
    
    # equals method to check whether other is equal to the given self argument and whether
    # self and other are the same type of variable
    def equals(self, other):
        if self == other and type(self) == type(other):
            return True
        else:
            return False

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.pizzas = []

    def display_menu():
        print("1. New Customer")
        print("2. Order Pizza")
        print("3. Display Orders")
        print("4. Finalise Orders")
        print("5. Exit")

    def display_second_menu():
        print("1. Change Size")
        print("2. Change Pizza Base")
        print("3. Add Topping")
        print("4. Remove Topping")
        print("5. Order")
        print("6. Cancel")

    def customer_name_input():
        customer_name = input("Please enter your name: ")
        return customer_name
    # add pizzas to the self._pizzas list (which is the receipt)
    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def create_receipt(self):
        # exception handling to check if any pizzas have been ordered so far
        if len(self.pizzas) == 0:
            print("No pizzas ordered so far.")
        else:      
            return self.pizzas

def main():
    print("---Welcome to the Pizza Shop---")
    print()
    
    customer_name = None
    order = None

    choice_selection = 0

    pizza_shop = PizzaShop()
    
    while choice_selection != 5:
        Order.display_menu()   
        try:
            choice_selection = int(input("How may I help you: "))
            if choice_selection < 1 or choice_selection > 5:
                print("Error: Input must be between 1 and 5")
        except ValueError as e:
            if type(choice_selection) != int:
                print("Input must be an integer")
            else:
                print("Error: Input value must be an integer")
            choice_selection = 0
            
        if choice_selection == 1 and customer_name is None:
            customer_name = Order.customer_name_input()
            print(f"Welcome to the Pizza Shop, {customer_name}!")
            order = Order(customer_name)  
        elif choice_selection == 2:
            print("Menu:")
            menu_items = pizza_shop.load_menu()
            for item in menu_items:
                print(f"- {item.getName()} - Price: {item.getPrice():.2f}:")
                print(f"  " + ", ".join(item.getToppings()))
            which_pizza = input("Which pizza would you like?")
            pizza_selected = None

            # Iterate through menu_items to find the selected pizza
            try:
                for item in menu_items:
                    if item.getName().lower() == which_pizza.lower():
                        pizza_selected = item
            except ValueError:
                print("Error occurred while processing your choice. Please try again.")

            # Check if the pizza has been found
            if pizza_selected:
                print(f"You selected: {pizza_selected.getName()}")
                
                # Display the second menu based on user's choice
                try:
                    Order.display_second_menu()
                    second_choice_selection = int(input("What would you like to do: "))
                except ValueError:
                    print("Invalid input. Please enter a valid option.")
                
                while second_choice_selection != 6:
                    if second_choice_selection == 1:
                        print("Available Sizes:")
                        print("1. Small")
                        print("2. Medium")
                        print("3. Large")
                        try:
                            size_choice = int(input("Select a size (1-3): "))
                            if 1 <= size_choice <= 3 and type(size_choice) == int:
                                # Update the pizza object's size based on the customer's choice
                                if size_choice == 1:
                                    pizza_selected.setSize("small")
                                elif size_choice == 2:
                                    pizza_selected.setSize("medium")
                                elif size_choice == 3:
                                    pizza_selected.setSize("large")
                                print(f"Size changed to: {pizza_selected.getPizzaSize()}")
                                print(pizza_selected.getPizzaSize())
                            else:
                                print("Invalid size choice.")
                        except ValueError:
                            print("Invalid input. Please enter a number (1-3).")
                    
                    elif second_choice_selection == 2:
                        print("Available Pizza Bases:")
                        print("1. Deep Pan")
                        print("2. Cheese Crust")
                        print("3. Thin Crust")

                        try:
                            base_choice = int(input("Select a pizza base (1-3): "))
                            # Convert the user's input to lowercase and compare
                            if 1 <= base_choice <= 3:
                                if base_choice == 1:
                                    pizza_shop.pizzaBase.setBase("deep pan")
                                elif base_choice == 2:
                                    pizza_shop.pizzaBase.setBase("cheese crust")
                                elif base_choice == 3:
                                    pizza_shop.pizzaBase.setBase("thin crust")
                                print(f"Pizza base changed to: {pizza_shop.pizzaBase.getBase()}")
                            else:
                                print("Invalid base choice.")
                        except ValueError:
                            print("Invalid input. Please enter a number (1-3).")
                    elif second_choice_selection == 3:
                        break
                    elif second_choice_selection == 4:
                        break
                    elif second_choice_selection == 5:
                        break
                    elif second_choice_selection == 6:
                        break

                    else:
                        print("Invalid choice. Please enter a number (1-6).")

                try:
                    Order.display_second_menu()
                    second_choice_selection = int(input("What would you like to do: "))
                except ValueError:
                    print("Invalid input. Please enter a valid option.")

        else:       
            print("Pizza not found in the menu.")






                            
                
        
                                











                #     elif second_choice_selection == 2:
                #         change pizza base
                #     elif second_choice_selection == 3:
                #         add topping
                #     elif second_choice_selection == 4:
                #         remove topping pop()
                #     elif second_choice_selection == 5:
                #         order
                    

    #     elif choice_selection == 3:
    #         # Display orders (pizzas in the order)
    #         if order is not None:
    #             print(f"Customer: {order.customer_name}")
    #             print("Orders:")
    #             for pizza in order.pizzas:
    #                 print(f"- {pizza.getName()} - Price: {pizza.getPrice()}")
    #         else:
    #             print("No orders placed yet.")
    #     elif choice_selection == 4:
    #      # Finalize orders (not implemented in the provided code)
    #         print("not done yet")
    #         # You can implement this part to calculate the total price and perform other actions.
            
    # print("Goodbye!")
    # testing the PizzaBase class

    # Order.display_menu()
    # size_input = int(input("Choose your pizza sizze(1 = small, 2 = medium, 3 = large):"))
    # b = PizzaBase(size_input, "cheese crust", size_input, 2.0)
    # print(b)
    # print(b.getName())
    # print(b)
    # print(b.getName())
    # # testing the PizzaShop class
    # print()
    # pizza_shop = PizzaShop()
    # pizza_shop.load_menu()
    # pizza_shop.load_ingredients()
    # print(pizza_shop)
    # p = PizzaShop()

if __name__ == '__main__':
    main()