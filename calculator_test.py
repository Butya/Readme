from unittest import TestCase
import unittest
from calculator import Calculator

class CalculatorTest(TestCase):
    def setUp(self):
        self.calc = Calculator()
		
	def testAdd(self):
        self.assertEqual(4, self.calc.add(2, 2))      # first test
        self.assertEqual(4, self.calc.add(-3, 7))     # second test
        self.assertEqual(4, self.calc.add(3,-7)) 	  # third test
		self.assertEqual(-10, self.calc.add(-3,-7)) 	  # fourth test
    def testSubtract(self):
        self.assertEqual(4, self.calc.subtract(6, 2))      # first test
        self.assertEqual(-8, self.calc.subtract(-6, 2))     # second test
        self.assertEqual(8, self.calc.subtract(6, -2)) # third test
		self.assertEqual(-4, self.calc.subtract(-6, -2)) # fourth test
		
    def testMultiply(self):
        self.assertEqual(4, self.calc.multiply(2, 2))      # first test
        self.assertEqual(-4, self.calc.multiply(-2, 2))     # second test
        self.assertEqual(4, self.calc.multiply(-2, -2)) # third test

		def testDivide(self):
        self.assertEqual(4, self.calc.divide(8, 2))      # first test
        self.assertEqual(-4, self.calc.divide(-8, 2))     # second test
        self.assertEqual(-4, self.calc.divide(8, -2)) # third test

if __name__ == '__main__':
    unittest.main()