import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(2, 3), 5)

    def test_divide(self):
        c = Calculator()
        self.assertEqual(c.divide(10, 2), 5.0)

if __name__ == '__main__':
    unittest.main()
