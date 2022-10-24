import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(2, 92), 94)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(2, 92), 0.021739130434782608)

        # testing for exception
        self.assertRaises(ValueError, calculator.divide, 10, 0)