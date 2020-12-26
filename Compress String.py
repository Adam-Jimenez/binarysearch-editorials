"""
Compress String

Groupby will group consecutive equal elements, so we can join the key from that group.
"""
from itertools import groupby
class Solution:
    def solve(self, s):
        return "".join(k for k,_ in groupby(s))