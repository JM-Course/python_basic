import unittest


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, n):
        self.value += n

    def sub(self, n):
        self.value -= n

    def clear(self):
        self.value = 0


class CalculatorTestCase(unittest.TestCase):
    def test_calculator(self):
        calculator = Calculator()
        calculator.add(3)
        self.assertEqual(calculator.value, 3)
        calculator.add(5)
        self.assertEqual(calculator.value, 8)
        calculator.sub(7)
        self.assertEqual(calculator.value, 1)
        calculator.clear()
        self.assertEqual(calculator.value, 0)


if __name__ == "__main__":
    unittest.main()
