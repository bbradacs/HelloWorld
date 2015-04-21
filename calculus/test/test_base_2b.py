import sys
sys.path.append('~/PycharmProjects/HelloWorld/calculus')

from calculus.base_2 import Calculation
from twisted.trial import unittest
from twisted.python import log

class CalculationTestCase(unittest.TestCase):
    def setUp(self)
        self.calc = Calculation()

    def tearDown(self)
        log.msg('tearDown() called')

    def _test(self, op, a, b, expected)
        result = op(a,b)
        self.assertEqual(result,expeced)

    def test_add(self):
        log.msg('createa a calculator')
        result = calc.add(3, 8)
        self._test(self.calc.add(3,8,11))

    def test_subtract(self):
        self._test(self.calc.subtract(7,3,4))

    def test_multiply(self):
        self._test(self.calc.multiply(6,9,54))

    def test_divide(self):
        self._test(self.calc.divide(12,5,2))

