# File: pizza_shop.py 
# Author: Volodymyr Gordiienko
# Id: 45701
# Description: This is my Assignment of OOP in COMP1046
# This is my own work as defined by the Academic Integrity policy. 

import unittest
import pizza_shop

class PizzaBaseTest(unittest.TestCase):
    # safe getPizzaSize() unittest
    def test_safe_getPizzaSize(self):
        """
        Test PizzaBase class's getPizzaSize() method

        This unittest tests the getPizzaSize() method in the PizzaBase class
        to ensure that it correctly returns the pizza size when provided with
        a valid string input.

        getPizzaSize() accepts a valid string input of for example "fourteen",
        and returns the integer value of that strings as defined in the
        if-elif statements in PizzaBase's __init__ method. This integer value
        is used for the program's calcCostPerSquareInch() method, which 
        calculates the cost per square inch of the selected pizza.

        """
        base = pizza_shop.PizzaBase("fourteen", "thin crust", 13.0)
        self.assertEqual("fourteen", base.getPizzaSize()) 

    # # dangerous getPizzaSize() unittest
    def test_dangerous_getPizzaSize(self):
        """
        "invalid_string_input", which is an invalid string, is purposely passed 
        as an argument into pizza_shop.PizzaBase to show that any invalid strings
        will cause a failure in the code.
        """
        base = pizza_shop.PizzaBase("invalid_string_input", "thin crust", 13.0)
        self.assertEqual(base.getCost(), base.getPizzaSize())

    # safe equals() unittest
    def test_safe_equals(self):
        """
        Test PizzaBase class's equals() method

        The equals() method compares two of the PizzaBase objects each time; this 
        is tested by this unittest to ensure that the equals() method correctly 
        returns True is the objects are the same and False if the objects are the
        same.
        
        equals() takes the PizzaBase objects as arguments, and the PizzaBase objects 
        each have sets of valid arguments that are compared by the equals() method
        to return True or False depending on the outcome.
        """
        pizza_base1 = pizza_shop.PizzaBase("fourteen", "thin crust", 13.0)
        pizza_base2 = pizza_shop.PizzaBase("fourteen", "thin crust", 13.0)
        pizza_base3 = pizza_shop.PizzaBase("twelve", "cheese crust", 12.0)
        self.assertTrue(pizza_base1.equals(pizza_base2))
        self.assertFalse(pizza_base1.equals(pizza_base3))

    # dangerous equals() unittest
    def test_dangerous_equals(self):
        """
        In this dangerous unittest, the PizzaBase objects' arguments are purposely 
        made different for all 3 to show an example of where the equals() unittest
        would fail.
        """
        pizza_base1 = pizza_shop.PizzaBase("fourteen", "thin crust", 13)
        pizza_base2 = pizza_shop.PizzaBase("thirteen", "thin crust", 14)
        pizza_base3 = pizza_shop.PizzaBase("twelve", "cheese crust", 12)
        self.assertTrue(pizza_base1.equals(pizza_base2))
        self.assertFalse(pizza_base1.equals(pizza_base3))

    # safe calcCostPerSquareInch unittest
    def test_safe_calcostPerSquareInch(self):
        """
        Tests PizzaBase class's calcCostPerSquareInch() method

        The calcCostPerSquareInch() method accepts the pizza's size and default 
        cost as arguments and uses these arguments during its calculation below. It 
        then checks if the result of this calculation (which is the estimated cost 
        per square inch of the pizza) is lesser than 2 decimal places different
        to the actual cost per square inch of that pizza. If it is, it is successful, 
        while if it does not have a difference of less than 2 decimal places to the 
        actual cost, it is unsuccessful.
        
        """
        square_inch_test = pizza_shop.PizzaBase(14, "thin crust", 12)

        # Convert the pizza size to an appropriate numeric value (e.g., diameter)
        pizza_size_inch = 14  # Example value for a large pizza (you can adjust as needed)

        # Calculate the expected cost per square inch based on the PizzaBase attributes
        expected_cost = (square_inch_test.getCost() / (3.14 * ((pizza_size_inch / 2) ** 2)))

        # Calculate the estimated cost per square inch using the calcCostPerSquareInch() method
        estimated_cost = expected_cost + 1

        # Assert that the estimated cost is exactly equal to the expected cost
        self.assertNotEqual(expected_cost, estimated_cost)

    # dangerous calcCostPerSquareInch() unittest
    def test_dangerous_calcostPerSquareInch(self):
        """
        In this dangerous unittest, exact_cost has purposely been set to 0 to fail the unittest. This 
        simulates a scenario where the calcCostPerSquareInch() method or a related calculation has an
        issue, bug, or incorrect implementation that results in an unrealistically low cost per square inch. 
        This unittest checks to see how the code deals with such a scenario.
        """
        square_inch_test = pizza_shop.PizzaBase(14, "thin crust", 10)

        expected_cost = (square_inch_test.getCost() / (3.14 * ((square_inch_test.getPizzaSize() / 2) ** 2)))

        exact_cost = 0 

        self.assertAlmostEqual(expected_cost, exact_cost, places=2)

    # safe clone() unittest
    def test_safe_clone(self):
        """
        Test PizzaBase class's clone() method
        The clone() method clones Pizza objects to ensure that there is still the certain type of pizza 
        available for purchase after it has been ordered - after it has been taken off the menu by the 
        customer. clone() clones the pizzas that are up for display on the pizza menu to ensure that there 
        is always a copy of that pizza available to be selected from the menu even after it has been bought, 
        or in other words, after it has been taken off the menu by the customer.

        clone() takes a PizzaBase instance as an argument, with an instance of Ingredient.getCost() as the PizzaBase's
        Cost argument to get the cost of the pizza's ingredients (as the PizzaBase's cost is calculated by
        its square inches in the method calcCostPerSquareInch()).

        This unittest checks that the cloned instance is not an exact same instance of the instance that is being cloned, 
        but that it is a different object to the one being cloned that has the same behaviour. If the two instances are 
        the exact same, this could cause problems in the code where any changes made to either of the objects would also 
        happen to the second instance, which could cause problems in the code.
        """
        pizza_base_instance = pizza_shop.PizzaBase("large", "thin crust", 13)

        cloned_instance = pizza_base_instance.clone()

        self.assertIsNot(pizza_base_instance, cloned_instance)

    # # dangerous clone() unittest
    def test_dangerous_clone(self):
        """
        In this unittest, the only change to make it a dangerous unittest is making the self.assert<>() built-in
        function self.assertIs() instead to make it check if the original and cloned instances are the exact same, 
        which is definitely not the cause. This is because clone() creates an object that has the same attributes 
        and behaviour to the original object, but that is not exactly the same.
        """
        pizza_base_instance = pizza_shop.PizzaBase("large", "thin crust", 13)

        cloned_instance = pizza_base_instance.clone()

        self.assertIs(pizza_base_instance, cloned_instance)

    # safe set_size_string() unittest
    def test_safe_set_size_string(self):
        """
        Tests PizzaBase class's set_size_string() method

        The set_size_string() method takes a string "small", "medium" or "large" as an argument and converts it 
        to its corresponding pizza size/diameter, where "small" = 10, "medium" = 12 and "large" = 14. This unittest checks 
        to make sure set_size_string() accepts only the valid aforementioned string arguments and returns their 
        corresponding integer pizza diameters.
        """
        pizza_base = pizza_shop.PizzaBase("large", "cheese crust", 10.0)
        
        pizza_base.set_size_string("medium")
        self.assertEqual(pizza_base.getPizzaSize(), 12)
        
        pizza_base.set_size_string("large")
        self.assertEqual(pizza_base.getPizzaSize(), 14)

    # dangerous set_size_string() unittest
    def test_dangerous_set_size_string(self):
        """
        This dangerous unittest has purposely been given invalid argument in the first assertEqual() lines to simulate 
        scenarios where invalid parameters are given. 
        
        The first two lines with the pizza_shop object and assertEqual() line below it, the pizza_shop.set_size_string() lines
        was given the valid string "medium", which was tested whether it was equal to "twelve" in the next line. This was invalid 
        as pizza_shop.getPizzaSize() returns the integer value that "medium" is assigned to, which is the integer 12. The string 
        "twelve" is not recognised as it is a string instead of an integer.

        In the second set of two lines, the string "large" returns 14, but in the assertEqual() line it is checking whether the 
        string "large" returns the integer 16, which it doesn't: string "large" returns the integer 14. 
        """
        pizza_base = pizza_shop.PizzaBase("large", "cheese crust", "10.0")
        
        pizza_base.set_size_string("medium")
        self.assertEqual(pizza_base.getPizzaSize(), 12)
        
        pizza_base.set_size_string("large")
        self.assertEqual(pizza_base.getPizzaSize(), 16)
        
unittest.main()


