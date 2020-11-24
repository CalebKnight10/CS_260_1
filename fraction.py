# Easy Frac Class
from __future__ import annotations

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    # Declare the instance __fields with type hints
    __num: int
    __den: int
    __sample: str

    def __init__(self, n: int = 0, d: int = 1):
        self.num: int = n
        self.den: int = d
        self.__sample = "No value"

    def __str__(self):
        return f"{self.__num}/{self.__den}"

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - \
            self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, other: Fraction):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other: Fraction):
        newnum = self.num * other.den / \
            self.den * other.num
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)


   # Getters for num and den
    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    # Setters for num and den (ONLY IF NEEDED)
    @num.setter
    def num(self, new_value: int):
        self.__num = new_value

    @den.setter
    def den(self, new_value: int):
        if new_value == 0:
            self.__den = 1
        else: self.__den = new_value

