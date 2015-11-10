from unittest import TestCase
from numbers import Numbers
import unittest

class NumbersTest(TestCase):
    def test_init(self):
        num = Numbers(1,2,3)
        self.assertEqual(1, num.a, 'A have wrong value')
        self.assertEqual(2, num.b, 'B have wrong value')
        self.assertEqual(3, num.c, 'C have wrong value')

if __name__ == '__main__':
    unittest.main()