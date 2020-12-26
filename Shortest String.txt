"""
Shortest String

If a zero and a one exist in s, it is always possible to find two of them that are side by side and delete them. Can i have upvotes too please?
"""
class Solution:
    def solve(self, s):
        return abs(s.count("1")-s.count("0"))