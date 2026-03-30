import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


class TestCalculator(unittest.TestCase):

    def test_general(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(divide(1, 2), 0.5)

    def test_addition(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
