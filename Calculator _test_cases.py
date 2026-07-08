import unittest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    # TC001: Addition of Two Positive Numbers
    def test_addition_positive(self):
        result = self.calc.add(15, 25)
        self.assertEqual(result, 40)
        print("TC001: Addition Test - PASSED ✅")
    
    # TC002: Subtraction with Negative Result
    def test_subtraction_negative(self):
        result = self.calc.subtract(10, 25)
        self.assertEqual(result, -15)
        print("TC002: Subtraction Test - PASSED ✅")
    
    # TC003: Multiplication
    def test_multiplication(self):
        result = self.calc.multiply(5, 4)
        self.assertEqual(result, 20)
        print("TC003: Multiplication Test - PASSED ✅")
    
    # TC004: Division
