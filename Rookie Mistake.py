"""
Rookie Mistake

Assuming there's always an R, if there's no B we can always reach the sides.
Otherwise, if the R is not trapped between two B's, we can reach one of the sides.
"""
class Solution:
    def solve(self, s):
        if "B" not in s: return True
        return not s.index("B") < s.index("R") < s.rindex("B")