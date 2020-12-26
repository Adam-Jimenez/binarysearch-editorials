"""
List Partitioning

Count the frequency of each color, then rebuild it in order. Apparently faster than rayz solution?
"""
from collections import Counter
class Solution:
    def solve(self, s):
        c=Counter(s)
        return ["red"]*c["red"]+["green"]*c["green"]+["blue"]*c["blue"]