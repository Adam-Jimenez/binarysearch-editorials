"""
Maximum Non-Adjacent Tree Sum

Classic dynamic programming problem, where our recurrence relation is defined by whether we use the current node or not.

If we use the current nodes, we cannot use the children therefore we have to jump over them.
If we do not use the current node, we are free to use the childrens in our final answer. 

There is O(2n) unique states (number of nodes times 2 states for the boolean), so this top-down algorithm runs in linear time.

This is the same as the problem House Robber III on Leetcode which I covered in this video: 
https://www.youtube.com/watch?v=1RAF6tW_Acs
"""
from functools import lru_cache
class Solution:
    def solve(self, root):
        @lru_cache(None)
        def dp(node, free=True):
            if not node: return 0
            ans = 0
            if free:
                ans = node.val + dp(node.left, False) + dp(node.right, False)
            ans = max(ans, dp(node.left, True) + dp(node.right, True))
            return ans
        return dp(root)