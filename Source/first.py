from math import pi
import json

class MyClass:
    def __init__(self,i):
            self.i = i


myClass = MyClass(3)

myClass.__class__

def fib(n):
    """
    :param n: documentation"""

    result = []
    a,b = 0,1
    while( a < n):
        print b
        a,b = b,a + b
        result.append(b)

    return result

f = lambda x : x + 1

result = fib(9)

if 8 in result:
    print result

print fib.__doc__

print f(3)
print "%.15f" %pi

print reduce (lambda x,y: x + y, range(1,11))
