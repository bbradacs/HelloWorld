# -*- test-case-name: calculus.test.test_base_2 -*-

import sys
sys.path.append('~/PycharmProjects/HelloWorld/calculus')




class Calculation(object):
    def _make_ints(self, *args):
        try:
            return map(int,args)
        except ValueError:
            raise TypeError("Couldn't coerce arguments to integers: %s" % args)

    def add(self, a, b):
        a,b = self._make_ints(a,b)
        return a + b

    def subtract(self, a, b):
        a,b = self._make_ints(a,b)
        return a - b

    def multiply(self, a, b):
        a,b = self._make_ints(a,b)
        return a * b

    def divide(self, a, b):
        a,b = self._make_ints(a,b)
        return (a / b)

