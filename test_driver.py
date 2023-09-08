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
    # safe setSize() unittest
    def test_setSize(self):
        set_size_test = pizza_shop.PizzaBase("large", "thin crust", 13.0)

        set_size_test.setSize(12)

        self.assertEqual(12, set_size_test.getPizzaSize())

    # def test_calcCostPerSquareInch(self):
    #     square_inch_test = pizza_shop.PizzaBase("large", "thin crust", "13.0")

    #     expected_cost = (float(square_inch_test.getCost()) / (3.14 * ((float(square_inch_test.getPizzaSize()) / 2) ** 2)))

    #     exact_cost = square_inch_test.calcCostPerSquareInch()

    #     self.assertAlmostEqual(expected_cost, exact_cost, places=2)

    # def test_clone(self):
    #     pizza_base_instance = pizza_shop.PizzaBase("large", "thin crust", 13)

    #     cloned_instance = pizza_base_instance.clone()

    #     self.assertIs(pizza_base_instance, cloned_instance)

    def test_set_size_string(self):
        # Create a PizzaBase object
        pizza_base = pizza_shop.PizzaBase("large", "thin crust", 13.0)

        # Test with a valid size string
        pizza_base.set_size_string("small")
        self.assertEqual(pizza_base.getPizzaSize(), 10)

        # Test with another valid size string
        pizza_base.set_size_string("medium")
        self.assertEqual(pizza_base.getPizzaSize(), 12)

        # Test with an invalid size string
        pizza_base.set_size_string("invalid_size")
        self.assertEqual(pizza_base.getPizzaSize(), 12)
        
unittest.main()

def add(x, y):
    return x, y

def divide(x):
    return 100/x

