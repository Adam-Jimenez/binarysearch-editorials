"""
Unique Fractions

Python has inbuilt fractions that simply fractions for you, and are hashable as well.
"""
from fractions import Fraction as frac
class Solution:
    def solve(self, fractions):
        s=set()
        for num,denum in fractions:
            f=frac(num,denum)
            s.add(f)
        return sorted([[f.numerator, f.denominator] for f in s],key=lambda x: x[0]/x[1])