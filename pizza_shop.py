# File: pizza_shop.py 
# Author: Volodymyr Gordiienko
# Id: 45701
# Description: This is my Assignment of OOP in COMP1046
# This is my own work as defined by the Academic Integrity policy. 

import math

class Ingredient:
    """Represents an ingredient used during the pizza selection.

    Initalises the attributes:
        float (Cost): The cost of the ingredient.
        str (Name): The name of the ingredient.
        str (formatPrice): The formatted price of the ingredient.
    """
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
        """
        Establishes the Ingredient --> PizzaBase aggregation relationship.

        Arguments:
            pizza_base (PizzaBase): The PizzaBase instance associated with this ingredient.
        """

        self.__pizza_base = pizza_base
    # getter method for self.__pizza_base
    def get_pizza_base(self):
        """
        Gets the associated PizzaBase instance created in the PizzaBase_aggregation method.

        Returns:
            The PizzaBase instance.
        """
        return self.__pizza_base
    # getter method for the private variable pizza_shop
    # for the Ingredient --> PizzaShop aggregation
    def get_pizza_shop(self):
        """
        Gets the PizzaShop instance.

        Returns:
            The PizzaShop instance.
        """
        return self.__pizza_shop
    # getter method for private variable self.__Cost
    def getCost(self):
        """
        Gets the cost of the ingredient.

        Returns:
            The cost of the ingredient as a float
        """
        return self.__Cost
    # getter method for private variable self.__name
    def getName(self):
        """
        Gets the name of the ingredient.

        Returns:
            The name of the ingredient as a string
        """
        return self.__Name
    # getter method for private variable self.__formatPrice
    def getFormatPrice(self):
        """
        Gets the formatted price of the ingredient.

        Returns:
            The formatted price of the ingredient as a string
        """
        return self.__formatPrice
    # clone method to return a copy of the ingredients used in a pizza or the additional
    # toppings selected by the customer
    def clone(self):
        """
        Creates a copy of the Ingredient.

        Returns:
            A copy of the Ingredient object.
        """
        cloned_ingredients = Ingredient(self.__Cost, self.__Name, self.__formatPrice)
        return cloned_ingredients
    # equals method to check whether other is equal to the given self argument and whether
    # self and other are the same type of variable
    def equals(self, other):
        """
        Checks if another object is equal to this ingredient.

        Arguments:
            The object to compare with this ingredient.

        Returns:
            True if the objects are equal, False otherwise.
        """
        if self == other and type(self) == type(other):
            return True
        else:
            return False
    # returns a string of the formatPrice starting with a $ sign and formatted
    # to 2 decimal places
    def displayFormatPrice(self):
        """
        Returns a string of the formatted price.

        Returns:
            The formatted price as a string.
        """
        return f"${self.__formatPrice:.2f}"

class PizzaShop:
    """
    Represents a pizza shop.

    Manages ingredients and pizzas.

    Attributes:
        dict (ingredients): A dictionary of ingredients.
        pizzaBase (PizzaBase): The default pizza base.
    """
    # PizzaBase's attributes are defined in PizzaShop's init method for the 
    # PizzaBase --> PizzaShop composition relationship
    def __init__(self):
        """
        Initializes a PizzaShop instance with an empty ingredients dictionary
        and a default pizza base.
        """
        # initialise an empty dictionary for ingredients
        self.ingredients = {}
        # PizzaBase --> PizzaShop composition relationship
        # an instance of PizzaBase is created in the init method
        self.pizzaBase = PizzaBase("large", "thin crust", 13.00)
    # Ingredient --> PizzaShop aggregation relationship method
    def add_ingredient_PizzaShop_aggregation(self, Name, Cost, formatPrice):
        """
        Adds an ingredient to the ingredients dictionary and establishes the 
        PizzaShop --> Ingredient association relationship.

        Arguments:
            str (Name): The name of the ingredient.
            float (Cost): The cost of the ingredient.
            str (formatPrice): The formatted price of the ingredient.
        """
        # association relationship (PizzaShop --> Ingredient)
        ingredient = Ingredient(Cost, Name, formatPrice)
        # adds an ingredient to the self.ingredients dictionary
        # using Name as a unique identifier parameter for each item 
        # in the dictionary
        self.ingredients[Name] = ingredient
    
    def add_ingredient_PizzaBase_aggregation(self, ingredient):
        """
        Creates the  aggregation relationship between PizzaBase and Ingredient.

        Args:
            ingredient (Ingredient): The Ingredient instance associated with the pizza base.
        """
        self.ingredients[ingredient]
        ingredient.PizzaBase_aggregation(self)
    def load_menu(self):
        """
        Reads the menu.txt file and returns it as a list of Pizza objects.

        Returns:
            list: A list of Pizza objects representing menu items.
        """
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
        """
        Reads the ingredients.txt file and returns it as two lists: one containing the pizza
        bases and the other containing the toppings.

        Returns:
            list: one list containing the pizza bases, the other containing the toppings.
        """
        filename = "ingredients.txt"

        try:
            # Open the ingredients.txt file for reading
            file = open(filename, "r")

            # Read the lines from the file
            lines = file.readlines()

            # Close the file
            file.close()

            # Create empty lists to store ingredients and pizza bases
            ingredients = []
            pizza_bases = []

            # Display the toppings, excluding lines starting with "base"
            print("Toppings:")
            for line in lines:
                if not line.strip().lower().startswith("base"):
                    ingredient_info = line.strip().split("$")
                    if len(ingredient_info) == 2:
                        name = ingredient_info[0].strip()
                        price = float(ingredient_info[1].strip())
                        ingredient = Ingredient(price, name, f"${price:.2f}")
                        ingredients.append(ingredient)
                        print(f"{name} ${price:.2f}")
                
                else:
                    pizza_base_info = line.strip().split("$")
                    if len(pizza_base_info) == 2:
                        name = pizza_base_info[0].strip()
                        price = float(pizza_base_info[1].strip())
                        pizza_base = PizzaBase("large", name, price)
                        pizza_bases.append(pizza_base)

            # Return both the ingredients and pizza bases
            return ingredients, pizza_bases

        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        
        except IOError:
            print(f"An error occurred while reading '{filename}'.")

    def __str__(self):
        """
        Returns the PizzaShop instance as a formated string (or f string).

        Returns:
            str: A string representation of the PizzaShop.
        """
        return f"Pizza Base: {self.name}, Price: ${self.price:.2f}"
    
class PizzaBase(Ingredient):
    """
    Represents a pizza base.

    This class inherits from Ingredient and therefore inherits all of Ingredient class's
    attributes and methods.

    Attributes:
        str (pizzaSize): The size of the pizza ("small", "medium" or "large").
        str (baseType): The type of pizza base.
        float (Cost): The cost of the pizza base.
    """
    def __init__(self, pizzaSize, baseType, Cost):
        """
        Initializes PizzaBase's attributes.

        Arguments:
            str (pizzaSize): The size of the pizza ("small", "medium" or "large").
            str (baseType): The type of pizza base.
            float (Cost): The cost of the pizza base.
        """
        super().__init__(Cost, baseType, "$" + str(Cost))
        self.__pizzaSize = pizzaSize
        self.__baseType = ["deep pan", "cheese crust", "thin crust"]

        if pizzaSize == "small":
            self.__pizzaSize = "small"
        elif pizzaSize == "medium":
            self.__pizzaSize = "medium"
        elif pizzaSize == "large":
            self.__pizzaSize = "large"

    def getPizzaSize(self):
        """
        Gets the size of the pizza.

        Returns:
            str: The size of the pizza.
        """
        return self.__pizzaSize
    
    def calcCostPerSquareInch(self):
        """
        Calculates the cost per square inch of the pizza base.

        Returns:
            float: The cost per square inch of the pizza base.
        """
        cost = float(self.getCost())
        pizza_size = float(self.__pizzaSize)
        cost_per_square_inch = float((cost/3.14) * ((pizza_size/2)**2))
        return cost_per_square_inch
    
    def setSize(self, newSize):
        """
        Sets the size of the pizza/initialises it in the test code to be changed throughout 
        the test code.

        Arguments:
            str (newSize): The new size of the pizza ("small", "medium" or "large").
        """
        self.__pizzaSize = newSize

    def getBase(self):
        """
        Returns the pizza's base.

        Returns:
            list: A list of available pizza base types or the selected pizza base in the test code.
        """
        return self.__baseType
    
    def setBase(self, newBase):
        """
        Sets the selected pizza base as the pizza base for the selected pizza in the test code.

        Arguments:
            str (newBase): The new type of pizza base.
        """
        self.__baseType = newBase
    # clone method to return a copy of the pizza base
    # use cloned for test code
    def clone(self):
        """
        Creates a copy of the pizza base.

        Returns:
            PizzaBase: A copy of the pizza base.
        """
        cloned_pizza_base = PizzaBase(self.__pizzaSize, self.__baseType, Ingredient.getCost(self))
        return cloned_pizza_base
    
    def set_size_string(self, newSize):
        """
        Converts the inputted size into an int for calculations of the pizza's price.

        Args:
            str (newSize): The new size of the pizza ("small", "medium" or "large").
        """
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
        """
        Checks if another object is equal to this pizza base.

        Arguments:
            other (object): The object to compare with this pizza base.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if type(self) == type(other) and \
            self.getCost() == other.getCost() and \
            self.getName() == other.getName() and \
            self.getPizzaSize() == other.getPizzaSize():
            return True
        else:
            return False

    def __str__(self):
        """
        Returns a string representation of the PizzaBase instance.

        Returns:
            str: A string representation of the PizzaBase.
        """
        if type(self) == type(other) and \
            self.getCost() == other.getCost() and \
            self.getName() == other.getName() and \
            self.getPizzaSize() == other.getPizzaSize():
            return True
        else:
            return False

class Pizza(PizzaBase):
    """
    Represents a pizza.

    This class inherits from PizzaBase and adds Pizza class's attributes and methods.

    Attributes:
        str (name): The name of the pizza.
        float (price): The price of the pizza.
        list (toppings): A list of toppings on the pizza.
    """
    def __init__(self, name, price, toppings):
        """
        Initializes a Pizza instance with the 3 attributes name, price and toppings.

        Arguments:
            str (name): The name of the pizza.
            float (price): The price of the pizza.
            list (topping): A list of toppings on the pizza.
        """
        super().__init__("large", "thin crust", 13.00)
        self.__price = price
        self.__name = name
        self.__toppings = []

    def getName(self):
        """
        Returns the name of the pizza.

        Returns:
            str: The name of the pizza.
        """
        return self.__name
    # getter method for the private variable self.__price
    def getPrice(self):
        """
        Returns the price of the pizza.

        Returns:
            float: The price of the pizza.
        """
        return self.__price
    
    def setTopping(self):
        """
        Set the toppings list to an empty list/initialises a toppings list
        for use in the test code.

        Returns:
            None
        """
        self.__toppings = []

    def addTopping(self, topping):
        self.__toppings.append(topping)
        """
        Adds a topping to the pizza in the test code.

        Arguments:
            str (topping): The topping to add.

        Returns:
            None
        """
    def removeToppings(self, topping):
        if topping in self.__toppings:
            self.__toppings.remove(topping)
        """
        Removes a topping from the pizza in the test code.

        Arguments:
            str (topping): The topping to remove.

        Returns:
            None
        """

    # getter method for the private variable self.__toppings
    def getToppings(self):
        """
        Returns the list of toppings on the pizza.

        Returns:
            list: List of toppings on the pizza.
        """
        return self.__toppings
    
    # clone method to create a copy of the pizza
    def clone(self):
        """
        Creates a copy of the pizza.

        Returns:
            A new Pizza object.
        """
        cloned_pizza = Pizza(self.price)
        return cloned_pizza
    
    # equals method to check whether other is equal to the given self argument and whether
    # self and other are the same type of variable
    def equals(self, other):
        """
        Compares one object to another object.

        Arguments:
            obj (Pizza): The other object to compare.

        Returns:
            bool: True if the two objects are equal, False otherwise.
         
        *This method is only used for the unittests*
        """
        if self == other and type(self) == type(other):
            return True
        else:
            return False

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.pizzas = []

    def display_menu():
        """
        Displays the first list of options when the customer walks into the pizza shop.
        """
        print("1. New Customer")
        print("2. Order Pizza")
        print("3. Display Orders")
        print("4. Finalise Orders")
        print("5. Exit")

    def display_second_menu():
        """
        Displays the second list of options when the customer has chosen a pizza - this
        list of options is for the customer to modify their selected pizza/each of their
        selected pizzas.
        """
        print("1. Change Size")
        print("2. Change Pizza Base")
        print("3. Add Topping")
        print("4. Remove Topping")
        print("5. Order")
        print("6. Cancel")

    def customer_name_input():
        """
        Accepts customer's name as input for the naming of the .txt file receipt.
        """
        customer_name = input("Please enter your name: ")
        return customer_name
    # add pizzas to the self._pizzas list (which is the receipt)
    def add_pizza(self, pizza):
        """
        Adds a pizza to the order.

        Arguments:
            pizza (Pizza): The pizza to add to the order.

        Returns:
            None
        """
        self.pizzas.append(pizza)

    def create_receipt(self):
        """
        Create a receipt of the order named as the customer's name with all the pizza's necessary attributes as selected by
        the customer.

        Returns:
            List of ordered pizzas as a list in a receipt.
        """
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
            
            for item in menu_items:
                if item.getName().lower() == which_pizza.lower():
                    pizza_selected = item
            print(f"You selected: {pizza_selected.getName()}")
            print(f"Your pizza: {pizza_selected.getName()} {pizza_selected.getPizzaSize()} {pizza_selected.setBase('large')} ${pizza_selected.getPrice():.2f}")
            print(f" {', '.join(pizza_selected.getToppings())}")

                # Display the second menu based on user's choice
            try:
                Order.display_second_menu()
                second_choice_selection = int(input("What would you like to do: "))
            except ValueError:
                print("Invalid input. Please enter a valid option.")
            # Check if the pizza has been found

            print(f"You selected: {pizza_selected.getName()}")
            while second_choice_selection != 6:
                if second_choice_selection == 1:
                    print("Available Sizes:")
                    print("1. Small")
                    print("2. Medium")
                    print("3. Large")
                    try:
                        valid_sizes = ["small", "medium", "large"]
                        size_choice = input("Select a size: ")
                        if size_choice.lower() in valid_sizes:
                            # Update the pizza object's size based on the customer's choice
                            if size_choice == "small":
                                pizza_selected.setSize("small")
                            elif size_choice == "medium":
                                pizza_selected.setSize("medium")
                            elif size_choice == "large":
                                pizza_selected.setSize("large")
                            print(f"Size changed to: {pizza_selected.getPizzaSize()}")
                            Order.display_second_menu()
                            second_choice_selection = int(input("What would you like to do: "))
                        else:
                            print("Invalid size choice.")
                    except ValueError:
                        print("Invalid input. Please enter a number (1-3).")
                elif second_choice_selection == 2:
                    if second_choice_selection == 2:
                        print("Bases:")
                        for base in pizza_shop.pizzaBase.getBase():
                            print(base.capitalize())
                        
                        base_choice = input("Select a pizza base: ").strip().lower()

                        # Check if the selected base choice is valid
                        valid_bases = []
                        for base in pizza_shop.pizzaBase.getBase():
                            valid_bases.append(base.lower())
                        if base_choice in valid_bases:
                            # Set the pizza base of the selected pizza to the chosen base
                            pizza_selected.setBase(base_choice)
                            print(f"Your pizza: {pizza_selected.getName()}, {pizza_selected.getPizzaSize()} {pizza_selected.getBase()} ${pizza_selected.getPrice():.2f}:")
                            # Display toppings on the next line
                            # print(f"empty list: {pizza_selected.setToppings()}")
                            print(f"Toppings {', '.join(pizza_selected.getToppings())}")
                            Order.display_second_menu()
                            second_choice_selection = int(input("What would you like to do: "))
                        else:
                            print("Invalid base choice. Please enter a valid base type.")
                            
                elif second_choice_selection == 3:
                    print("Toppings:")
                    pizza_shop.load_ingredients()
                    pizza_instance = Pizza(item.getName(), item.getPrice(), item.getToppings())
                    toppings_selection = input("What topping would you like to add: ")
                    
                    # Check if the selected topping is valid
                    if toppings_selection.lower() in pizza_shop.load_ingredients():
                        # Add the topping to the selected pizza
                        pizza_instance.addTopping(toppings_selection)

    else:       
        print("Pizza not found in the menu.")

if __name__ == '__main__':
    main()