"""
Line of People

If there are at most b people behind you, your position can vary between 0 and b+1 (+1 because you are at the position after the bth person). If at least a people are in front of you, your position varies between 0 and n-a.
"""
class Solution:
    def solve(self, n, a, b):
        return min(n-a,b+1)
