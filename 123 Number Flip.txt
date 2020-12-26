"""
123 Number Flip

We want to find the leftmost digit that isn't a three and flip it to a three.

The reason it works is that every increase in value in a digit to the left increase the value 10 times more than the next digit.
"""
class Solution:
    def solve(self, n):
        i=0
        s=str(n)
        for i,c in enumerate(str(n)):
            if s[i]!="3":
                s=s[:i]+"3"+s[i+1:]
                break
        return int(s)
