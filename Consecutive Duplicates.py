"""
Consecutive Duplicates

Python's groupby function groups consecutive equals value for you. Why do any work when python does it for you?

"""
from itertools import groupby
class Solution:
    def solve(self, s):
        return "".join(k for k,_ in groupby(s))
