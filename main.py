import fraction
from fraction import Fraction
import sys


def main():
    print ("This is Main")
    f = Fraction(1, 2)
    g = Fraction(2, 3)
    d = Fraction(0, 0)
    print("f= ", f)
    print("f * g= ", f*g)
    print("d=" , d)
    print("f + d= ", f+d)
    print("f - d= ", f-d)
    print("f / d= ", f/d)
    d.num = 45
    d.den = 143
    print("New d= ", d)
    print("New f + d=", f+d)
    print("New f - d=", f-d)
    print("New f / d= ", f/d)


main()