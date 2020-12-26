"""
Non-Consecutive String

We can represent this problem as a tree, where every node represent a chosen character. The root of this tree will have three possibilities, then every node will have two options (to avoid repetition). 

We can avoid exploring subtrees unnecessarily by counting the number of nodes under it. Since we know the levels left for the tree (s) and how many children each node has (2**(s-1), because we double the number of nodes per level), we know that if the number of nodes in a subtree is less than k, we don't have to explore that subtree.

Similar to https://leetcode.com/problems/permutation-sequence/
"""
class Solution:
    def solve(self, s, k,last=None):
        if s == 0: return ""
        for c in "012":
            if c == last: continue
            if k<2**(s-1):
                return c + self.solve(s-1, k, c)
            k -= 2**(s-1)
        return ""
