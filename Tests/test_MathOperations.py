import unittest

from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Multiplication import Multiplication
from MathOperations.Division import Division

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    #def test_MathOperations_AdditionList(self):
     #   list = [1, 2, 3]
     #  self.assertEqual(6, Addition.sumList(list))

    def test_MathOperations_Subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_Multiplication(self):
        self.assertEqual(4, Multiplication.product(2, 2))

    def test_MathOperations_Division(self):
        self.assertEqual(2, Division.quotient(4, 2))

if __name__ == '__main__':
    unittest.main()
