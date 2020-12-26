"""
String Isomorphism

Since each unique character in S should equal one unique character in T and vice versa, we can check that the number of unique pairs of corresponding letters equal the number of unique characters in S and T.
"""
class Solution:
    def solve(self, s, t):
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))