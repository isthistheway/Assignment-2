# File: pizza_shop.py 
# Author: Volodymyr Gordiienko
# Id: 45701
# Description: This is my Assignment of OOP in COMP1046
# This is my own work as defined by the Academic Integrity policy. 

# Week 8 Lecture - Docstrings and Pytest
import unittest
import pizza_shop

class PizzaBaseTest(unittest.TestCase):
    # safe getPizzaSize() unittest
    def test_getPizzaSize(self):
        base = pizza_shop.PizzaBase("fourteen", "thin crust", 13.0)
        self.assertEqual("fourteen", base.getPizzaSize()) 
    # safe equals() unittest
    def test_equals(self):
        pizza_base1 = pizza_shop.PizzaBase("fourteen", "thin crust", 13.0)
        pizza_base2 = pizza_shop.PizzaBase("fourteen", "thin crust", 13.0)
        pizza_base3 = pizza_shop.PizzaBase("twelve", "cheese crust", 12.0)

        self.assertTrue(pizza_base1.equals(pizza_base2))  # Should be True because they have the same attributes
        self.assertFalse(pizza_base1.equals(pizza_base3))

    # safe calcCostPerSquareInch unittest
    def test_calcostPerSquareInch(self):
        square_inch_test = pizza_shop.PizzaBase("large", "thin crust", 10)

        expected_cost = (square_inch_test.getCost() / (3.14 * ((square_inch_test.getPizzaSize() / 2) ** 2)))
        
        exact_cost = round(square_inch_test.getCost(), 2)/square_inch_test.calcCostPerSquareInch()

        self.assertAlmostEqual(expected_cost, exact_cost, places=2)
        print(expected_cost, exact_cost)

    def test_clone(self):
        pizza_base_instance = pizza_shop.PizzaBase("large", "thin crust", 13)

        cloned_instance = pizza_base_instance.clone()

        self.assertIsNot(pizza_base_instance, cloned_instance)

    def test_set_size_string(self):
        # Create a PizzaBase object
        pizza_base = pizza_shop.PizzaBase("large", "cheese crust", 10.0)
        
        # Test with a valid size string
        pizza_base.set_size_string("medium")
        self.assertEqual(pizza_base.getPizzaSize(), 12)
        
        # Test with an invalid size string
        pizza_base.set_size_string("large")
        self.assertEqual(pizza_base.getPizzaSize(), 14)
        
unittest.main()

def add(x, y):
    return x, y

def divide(x):
    return 100/x

