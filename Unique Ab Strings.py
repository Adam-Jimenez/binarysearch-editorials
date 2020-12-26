"""
Unique Ab Strings

Each a has two possibilities: a or b. So each time we encounter an "a", we double the number of possibilities.

We can express this with an base 2 exponential.
"""
class Solution:
    def solve(self, s):
        return 2**s.count("a")%(10**9+7)
