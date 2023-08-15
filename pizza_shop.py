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

    def getCost(self):
        return self.__Cost
    
    def getName(self):
        return self.__Name
    
    def getFormatPrice(self):
        return self.__formatPrice
    
    def displayFormatPrice(self):
        return f"{self.__formatPrice}"

class PizzaBase(Ingredient):
    def __init__(self, pizzaSize, baseType, user_input):
        super().__init__(self, self.__Cost, self.__Name, self.__formatPrice)
        self.__pizzaSize = pizzaSize
        self.__baseType = baseType

        if user_input == 1:
            self.__size = 10
        elif user_input == 2:
            self.__size = 12
        elif user_input == 3:
            self.__size = 14
        else:
            print("Invalid input: can only choose 1, 2 or 3.")
    def getPizzaSize(self):
        return self.__pizzaSize
    
    def calcSquareInch(self):
        return None
    
    def calcCostPerSquareInch(self):
        return None
    
    def setSize(self, newSize):
        self.__pizzaSize = newSize

    def getBase(self):
        return self.__baseType
    
    def setBase(self, newBase):
        self.__baseType = newBase

    def __str__(self):
        return "PizzaBase" + self.__Name() + " " + str(self.__size)

class Pizza(PizzaBase):
    super().__init__(self, self.price)
    def __init__(self, toppings, crusts, price):
        super().__init__(self, self.)
        self.__toppings = []
        self.__crusts = crusts
        self.__price = price
        self.size = "large"
        self.base = "thin crust"

    # getter method for the private variable self.__price
    def getPrice(self):
        return self.__price
    
    def setCrusts(self):
        self.__crusts = "thin curst"

    def getCrusts(self):
        return self.__crusts
    
    def setTopping(self):
        self.__toppings = []

    def addTopping(self, topping):
        self.__toppings.append(topping)

    def removeToppings(self, topping):
        self.__toppings.remove(topping)

    # getter method for the private variable self.__toppings
    def getToppings(self):
        return self.__toppings

class PizzaShop:
    def __init__(self):
        self.pizza_menu = PizzaMenu()
        # initialise an empty dictionary for ingredients
        self.ingredients = {}
    
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
        lines = open_ingredients.readlines()
        # remove any blank space characters or extra spaces
        lines = lines.strip()
        # split the line to separate the name and price by the dollar symbol - the name and price get put into a list 
        # with the split() function and can then be accessed with index positions and the $ sign is not included in 
        # the list
        no_dollar_sign = lines.split("$")
        # the name will always be [0] in the list and price will always be [1] in the list
        for eachLine in filename:
            if len(no_dollar_sign) == 2:
                # set the ingredient name to the name
                name = no_dollar_sign[0].strip()
                # set the ingredient price to the price
                price = float(no_dollar_sign[1].strip())
                # checks to see if the line starts with the word base and if it does, 
                # it makes it a PizzaBase
                if len(name) >= 4 and name[:4].lower() == "base":
                    ingredient = PizzaBase(name, price)
                else:
                    # if the line doesn't start with the word base, it makes it a
                    # Food object with the name and price
                    ingredient = Food(name, price)
                
                ingredients.append(ingredient)
                self.ingredients[name] = ingredient
        # close the ingredients.txt file
        open_ingredients.close()

        return ingredients

    def __str__(self):
        return f"Pizza Base: {self.name}, Price: ${self.price:.2f}"

def main():
    print("---Welcome to the Pizza Shop---")
    print()
    # customer_name_input = input("Please enter your name to get started!")
    # testing the PizzaBase class
    user_input = int(input("Choose your pizza sizze(1 = small, 2 = medium, 3 = large):"))
    b = PizzaBase("cheesy crust", 14, "pepperoni", user_input)
    print(b)
    print(b.get_name())
    b.set_name("thin crust")
    print(b)
    print(b.get_name())
    # testing the PizzaShop class
    print()
    pizza_shop = PizzaShop("vlad")
    pizza_shop.load_menu()
    pizza_shop.load_ingredients()
    print(pizza_shop)
    p = PizzaShop()

if __name__ == '__main__':
    main()