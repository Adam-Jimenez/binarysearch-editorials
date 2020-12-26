"""
String Addition

Lazy method: cast the strings to int, evaluate the addition and cast back to string.
"""
class Solution:
    def solve(self, a, b):
        return str(int(a)+int(b))
