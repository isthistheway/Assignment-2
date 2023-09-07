# File: pizza_shop.py 
# Author: Volodymyr Gordiienko
# Id: 45701
# Description: This is my Assignment of OOP in COMP1046
# This is my own work as defined by the Academic Integrity policy. 

# Week 8 Lecture - Docstrings and Pytest
import unittest
import pizza_shop

# class PizzaBaseTest(unittest.TestCase):
#     def test_get_diameter(self):
#         base = pizza_shop.PizzaBase("thin crust", 8, 14, 16)
#         self.assertEqual(14, self.__pizzaSize)

class PizzaBaseTest(unittest.TestCase):
    def test_get_diameter(self):
        base = pizza_shop.PizzaBase("TestPizza", "medium", 12, 10.0)
        self.assertEqual(12, base.getPizzaSize()) 

class PizzaBaseTest(unittest.TestCase):
    def test_get_diameter(self):
        base = pizza_shop.PizzaBase("TestPizza", "medium", "twelve", 10.0)
        self.assertEqual("twelve", base.getPizzaSize())   
unittest.main()

def add(x, y):
    return x, y

def divide(x):
    return 100/x

