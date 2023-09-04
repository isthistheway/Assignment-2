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
    # aggregation relationship between Ingredient and PizzaShop
    # (Ingredient --> PizzaShop)
    def PizzaShop_aggregation(self, pizza_shop):
        self.__pizza_shop = pizza_shop
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
    def __init__(self, pizzaSize, baseType, size_input, price):
        # initialise an empty dictionary for ingredients
        self.ingredients = {}
        # PizzaBase --> PizzaShop composition relationship
        # an instance of PizzaBase is created in the init method
        self.pizzaBase = PizzaBase(pizzaSize, baseType, size_input, price)
    # Ingredient --> PizzaShop aggregation relationship method
    def add_ingredient_PizzaShop_aggregation(self, Name, Cost, formatPrice):
        # association relationship (PizzaShop --> Ingredient)
        ingredient = Ingredient(Cost, Name, formatPrice)
        # aggregation relationship between Ingredient and PizzaShop
        # (Ingredient --> PizzaShop)
        ingredient.PizzaShop_aggregation(self)
        # adds an ingredient to the self.ingredients dictionary
        # using Name as a unique identifier parameter for each item 
        # in the dictionary
        self.ingredients[Name] = ingredient
    
    def add_ingredient_PizzaBase_aggregation(self, ingredient):
        self.ingredients.append(ingredient)
        ingredient.PizzaBase_aggregation(self)
    def load_menu(self):
        # load the ingredients first before the menu
        self.load_ingredients()
        # set open_menu to a variable
        open_menu = open("menu.txt", "r")
        # opens the menu.txt file for reading and all the text file contents
        # a list of strings
        lines = open_menu.readlines()        
        # makes each line a list with the name of the pizza and all the ingredients as 2 total
        # list elements for each list
        for eachLine in lines:
            eachLine = eachLine.strip()
            pizza_info = eachLine.split(' $')
            print(pizza_info)
            name = pizza_info[0]
            string_price = pizza_info[1][:2]
            index = 0
            print(name)
            price = float(string_price)
            print(string_price)
            toppings = pizza_info[1][3:]
            print(toppings)

            pizza_info_separated = []
            pizza_info_separated.append(name)
            print(pizza_info_separated)
            pizza_info_separated.append(price)
            pizza_info_separated.append(toppings)
            print(pizza_info_separated)

        return Pizza(name, price, toppings)
    
    def load_ingredients(self):
        filename = "ingredients.txt"
        # open the ingredient.txt file for reading
        open_ingredients = open(filename, "r")
        # make the ingredient list an empty list
        ingredients = []
        # read every line of the text file and return it as a list of strings
        
        for eachLine in open_ingredients:
            lines = open_ingredients.readlines()

            print(lines)
            # remove any blank space characters or extra spaces
            lines = lines.strip()
            # split the line to separate the name and price by the dollar symbol - the name and price get put into a list 
            # with the split() function and can then be accessed with index positions and the $ sign is not included in 
            # the list
            split_lines = lines.split("$")
            if len(split_lines) == 2:
                # set the ingredient name to the name
                name = split_lines[0].strip()
                # set the ingredient price to the price
                price = float(split_lines[1].strip())
                # checks to see if the line starts with the word base and if it does, 
                # it makes it a PizzaBase
                if len(name) >= 4 and name[:4].lower() == "base":
                    # PizzaBase --> PizzaShop composition relationship
                    ingredient = PizzaBase(name, price)
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
    def __init__(self, pizzaSize, baseType, size_input, price):
        super().__init__(price, baseType, "$" + str(price))
        self.__pizzaSize = pizzaSize
        self.__baseType = ["deep pan", "cheese crust", "thin crust"]

        if size_input == 1:
            self.__size = 10
        elif size_input == 2:
            self.__size = 12
        elif size_input == 3:
            self.__size = 14
        else:
            print("Invalid input: can only choose 1, 2 or 3.")

    def getPizzaSize(self):
        return self.__pizzaSize
   
    def calcCostPerSquareInch(self):
        cost_per_square_inch = float((self.__Cost/3.14) * (self.__size/2)^2)
        return cost_per_square_inch
    
    def setSize(self, newSize):
        self.__pizzaSize = newSize

    def getBase(self):
        return self.__baseType
    
    def setBase(self, newBase):
        self.__baseType = newBase
    # clone method to return a copy of the pizza base

    def clone(self):
        cloned_pizza_base = PizzaBase(self.__pizzaSize, self.__baseType, user_input)
        return cloned_pizza_base
    
    # equals method to check whether other is equal to the given self argument and whether
    # self and other are the same type of variable
    def equals(self, other):
        if self == other and type(self) == type(other):
            return True
        else:
            return False
        
    def __str__(self):
        return "PizzaBase" + self.getName() + " " + str(self.__size)

class Pizza(PizzaBase):
    def __init__(self, price):
        super().__init__(self, self.__pizzaSize, self.__baseType)
        self.__price = price
        # self.__toppings = []
        # self.__crusts = crusts
        self.size = "large"

    # getter method for the private variable self.__price
    def getPrice(self):
        return self.__price
    
    def setTopping(self):
        self.__toppings = []

    def addTopping(self, topping):
        self.__toppings.append(topping)

    def removeToppings(self, topping):
        self.__toppings.remove(topping)
    # clone method to create a copy of the pizza
    def clone(self):
        cloned_pizza = Pizza(self.__price)
        return cloned_pizza
    
    # equals method to check whether other is equal to the given self argument and whether
    # self and other are the same type of variable
    def equals(self, other):
        if self == other and type(self) == type(other):
            return True
        else:
            return False
        
    # getter method for the private variable self.__toppings
    def getToppings(self):
        return self.__toppings

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.pizzas = []

    def customer_name_input(self):
        customer_name = input("Please enter your name: ")
        return customer_name
    # add pizzas to the self._pizzas list (which is the receipt)
    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def create_receipt(self):
        # exception handling to check if any pizzas have been ordered so far
        try:
            if len(self.pizzas) == 0:
                print("No pizzas ordered so far.")
        except IndexError as e:
            print("Error: ", e)

def display_menu():
        print("1. New Customer")
        print("2. Order Pizza")
        print("3. Display Orders")
        print("4. Finalise Orders")
        print("5. Exit")

def main():
    print("---Welcome to the Pizza Shop---")
    print()
    customer_name = None
    order = None

    choice_selection = 0

    while choice_selection != 5:
        display_menu    
        try:
            choice_selection = int(input("How may I help you: "))
        except ValueError:
            print("Error: Must enter an integer between 1 and 5.")
            choice_selection = 0
            continue
    
        if choice_selection == 1 and customer_name == None:
            customer_name = Order.customer_name_input()
            print(f"Welcome to the Pizza Shop, {customer_name}!")
            order = Order(customer_name)   
        elif choice_selection and customer_name != None:
            print(f"Welcome back to the Pizza Shop, {customer_name}!")
            order = Order(customer_name)

        #elif choice_selection == 2 and order == None:

    

    
    # testing the PizzaBase class
    size_input = int(input("Choose your pizza sizze(1 = small, 2 = medium, 3 = large):"))
    b = PizzaBase(size_input, "cheese crust", size_input, 2.0)
    print(b)
    print(b.getName())
    print(b)
    print(b.getName())
    # testing the PizzaShop class
    print()
    pizza_shop = PizzaShop()
    pizza_shop.load_menu()
    pizza_shop.load_ingredients()
    print(pizza_shop)
    p = PizzaShop()

if __name__ == '__main__':
    main()