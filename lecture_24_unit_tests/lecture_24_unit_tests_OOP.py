import unittest


class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def subtract(self):
        return self.first - self.second


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator(first=1, second=2)
        print("setUp method called")

    def tearDown(self):
        del self.calculator
        print("tearDown method called")

    def test_add(self):
        self.assertEqual(self.calculator.add(), 3)
        self.calculator.first = 15
        self.assertEqual(self.calculator.add(), 17)
        print("test_add method called")

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(), -1)
        self.calculator.first = 15
        self.assertEqual(self.calculator.subtract(), 13)
        print("test_subtract method called")


if __name__ == '__main__':
    unittest.main()
