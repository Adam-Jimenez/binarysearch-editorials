"""
Overchoice

Sexy one-liner: we replace all "[" with "]", then we can split over all "]". Then, for all strings in the result, if there is the character "|", we split it, otherwise we return the string in a list [s]. Then the product function will generate all products like the problem describes. We join and sort the result.
"""
from itertools import product
class Solution:
    def solve(self, s):
        return sorted(["".join(a) for a in product(*[s.split("|") if "|" in s else [s] for s in filter(None,s.replace("[","]").split("]"))])])