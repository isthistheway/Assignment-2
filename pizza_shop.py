# File: pizza_shop.py 
# Author: Volodymyr Gordiienko
# Id: 45701
# Description: This is my Assignment of OOP in COMP1046
# This is my own work as defined by the Academic Integrity policy. 

import math

class Pizza:
    def __init__(self, toppings, cheeseType, price, presets):
        self.__toppings = toppings
        self.__cheeseType = cheeseType
        self.__price = price
        self.__presets = presets
    # getter method for the private variable self.__price
    def getPrice(self):
        return self.__price
    
    def setTopping(self):
        self.__toppings = []

    def addTopping(self):
        self.__toppings.append()
    # getter method for the private variable self.__toppings
    def getToppings(self):
        return self.__toppings

    def removeToppings(self):
        self.__toppings.remove()

    def setCheese(self):
        self.__cheeseType = []
    # getter method for the private variable self.__cheeseType       
    def getCheese(self):
        return self.__cheeseType

    def setPresets(self):
        self.__presets = ["Meat Lovers" : ["Pepperoni", "Sausage", "Bacon", \
  "Gound_beef", "Ham", "Mozzarella", 11, "Classic Crust", 14.99], \
  "Double Bacon Cheeseburger" : ["Bacon", "Ground_beef", \
  "Mozzarella", 11, "Classic Crust", 14.99]
  "Pepperoni" : ["Pepperoni", "Mozzarella", 11, "Classic Crust", 7.00], \
  "Ham & Cheese" : ["Ham","Mozzarella", 11, "Classic Crust", 7.00], \
  "Cheese" : ["Mozzarella", 11, "Classic Crust", 7.00]]
    
    def getPresets(self):
        return self.__presets

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class PizzaBase(Food, Pizza):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        super().__init__(self, name, price, self.__toppings, self.__cheeseType, self.__price, self.__presets)

    def load_ingredients(self):
        filename = "ingredients.txt"
        # open the ingredient.txt file for reading
        open_ingredients = open(filename, "r")
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
                if len(name) >= 4 and name[:4].lower() == "base":
                    return PizzaBase(name, price)
                else:
                    return Food(name, price)
        # close the ingredients.txt file
        open_ingredients.close()

    def load_menu(self):
        open_menu = open("menu.txt", "r")
        # opens the menu.txt file for reading and makes everything a list of strings
        lines = open_menu.readlines()
        # removes any unwanted space or blank space characters
        stripped_lines = lines.strip()
        # makes each line a list with the name of the pizza and all the ingredients as 2 total
        # list elements for each list
        split_lines = stripped_lines.split("$")
        for eachLine in stripped_lines:
            name = split_lines[0].strip()
            price = split_lines[1].strip()
            toppings = split_lines[2].strip()
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

class PizzaShop:
    def __init__(self, manager, employee_list, pizzaShopStatus):
        self.__manager = manager
        self.__employee_list = employee_list
        self.__pizzaShopStatus = ["Open", "Closed"]

    def open(self):
        self.__pizzaShopStatus == "Open"
    
    def operate(self):
        if self.__pizzaShopStatus == "Open":
            return None
        else:
            print("Cannot operate: pizza shop is currently closed.")

class Employee:
    def __init__(self, employee_name, employee_age, employee_id, baseWage, hours_worked):
        self.__employee_name = employee_name
        self.__employee_age = employee_age
        self.__employee_id = employee_id
        self.__baseWage = baseWage
        self.hours_worked = hours_worked

    def work(self):
        self.hours_worked += <number of hours>
    
    def get_paid(self):
        total_money = self.__baseWage * self.hours_worked
        return total_money

class Interface:
    def __init__(self, pizza_menu, pizza_bases, current_toppings, extra_toppings_options):
        self.__pizza_menu = pizza_menu
        self.__pizza_bases = pizza_bases
        self.__current_toppings = current_toppings
        self.__extra_toppings_options = extra_toppings_options

    def accept_input(self):
        return None
    
    def displayReceipt(self):
        print
    
class OrderingSystem(Interface):
    def __init__(self, txt_file):
        super().__init__(self.__pizza_menu, self.__pizza_bases, self.__current_toppings, self.__extra_toppings_options)
        self.__txt_file = ""
    
    def writeToFile(self):
        text_file = self.__txt_file
        text_file += <finalised order>

    def place_order(self):
        return None

def main():
    print("---Welcome to the Pizza Shop---")
    print()

# WARNING: Do not write any code in global scope

if __name__ == '__main__':
    main()