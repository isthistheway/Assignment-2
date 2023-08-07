# File: pizza_shop.py 
# Author: Volodymyr Gordiienko
# Id: 45701
# Description: This is my Assignment of OOP in COMP1046
# This is my own work as defined by the Academic Integrity policy. 

import math

class Food:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class PizzaBase(Food):
    def __init__(self, name, price, size, user_input):
        super().__init__(name, price)
        self.__size = size
        self.user_input = user_input
        if user_input == 1:
            self.__size = 10
        elif user_input == 2:
            self.__size = 12
        elif user_input == 3:
            self.__size = 14
        else:
            print("Invalid input: can only choose 1, 2 or 3.")

    def __str__(self):
        return "PizzaBase" + self.get_name() + " " + str(self.__size)

class Pizza(PizzaBase):
    def __init__(self, toppings, crusts, price):
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
    
class PizzaMenu:
    def __init__(self, menu):
        self.menu = []
    
    def addPizza(self, pizza):
        self.menu.append(pizza)

class PizzaShop:
    def __init__(self):
        self.pizza_menu = PizzaMenu()
        self.ingredients = {}
    
    def load_menu(self):
        # load the ingredients first before the menu
        self.load_ingredients()
        # set the open() statement to a variable
        open_menu = open("menu.txt", "r")
        # opens the menu.txt file for reading and makes everything a list of strings
        lines = open_menu.readlines()
        # removes any unwanted space or blank space characters
        stripped_lines = lines.strip()
        # makes each line a list with the name of the pizza and all the ingredients as 2 total
        # list elements for each list
        split_lines = stripped_lines.split("$")
        for eachLine in stripped_lines:
            name_and_price = eachLine[1].split()
            name = name_and_price[0]
            price = float(name_and_price[1])
            toppings = name_and_price[2:]

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
                    ingredients.append(PizzaBase(name, price))
                else:
                    # if the line doesn't start with the word base, it makes it a
                    # Food object with the name and price
                    ingredients.append(Food(name, price))
        # close the ingredients.txt file
        open_ingredients.close()

        return ingredients

    def __str__(self):
        return f"Pizza Base: {self.name}, Price: ${self.price:.2f}"
    
class PizzaTopping:
    def __init__(self, toppingCost, toppingName, toppingID):
        self.__toppingCost = toppingCost
        self.__toppingName = toppingName
        self.__toppingID = toppingID

    def getToppingCost(self):
        return self.__toppingCost
    
    def getToppingName(self):
        return self.__toppingName
    
    def getToppingID(self):
        return self.__toppingID
    
class Ingredient(PizzaTopping):
    def __init__(self, ingredientCost, ingredientID, ingredientName, formatPrice):
        super().__init__(self, self.__toppingCost, self.__toppingName, self.__toppingID)

        self.__ingredientCost = ingredientCost
        self.__ingredientID = ingredientID
        self.__ingredientName = ingredientName
        self.__formatPrice = formatPrice

    def getIngredientCost(self):
        return self.__ingredientCost
    
    def getIngredientID(self):
        return self.__ingredientID
    
    def getIngredientName(self):
        return self.__ingredientName
    
    def getFormatPrice(self):
        return self.__formatPrice
    
    def displayFormatPrice(self):
        print(self.__formatPrice)



# class Employee:
#     def __init__(self, employee_name, employee_age, employee_id, baseWage, hours_worked):
#         self.__employee_name = employee_name
#         self.__employee_age = employee_age
#         self.__employee_id = employee_id
#         self.__baseWage = baseWage
#         self.hours_worked = hours_worked

#     def work(self):
#         self.hours_worked += <number of hours>
    
#     def get_paid(self):
#         total_money = self.__baseWage * self.hours_worked
#         return total_money

class Interface:
    def __init__(self, pizza_menu, current_toppings, extra_toppings_options):
        self.__pizza_menu = pizza_menu
        self.__current_toppings = current_toppings
        self.__extra_toppings_options = extra_toppings_options

    def accept_input(self):
        return None
    
    def displayReceipt(self):
        print
    
class OrderingSystem(Interface):
    def __init__(self, txt_file):
        super().__init__(self.__pizza_menu, self.__current_toppings, self.__extra_toppings_options)
        self.__txt_file = ""
    
    def writeToFile(self):
        text_file = self.__txt_file
        # text_file += <finalised order>

    def place_order(self):
        return None

def main():
    print("---Welcome to the Pizza Shop---")
    print()
    user_input = int(input("Choose your pizza sizze(1 = small, 2 = medium, 3 = large):"))
    b = PizzaBase("cheesy crust", 14, "pepperoni", user_input)
    print(b)
    print(b.get_name())
    b.set_name("thin crust")
    print(b)
    print(b.get_name())

if __name__ == '__main__':
    main()