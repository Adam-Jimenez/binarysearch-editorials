"""
Sort by Permutation

Solution for the lazies like me: create pairs using (p[i], lst[i]), sort them build an array from lst[i].
"""
class Solution:
    def solve(self, lst, p):
        return [x for _,x in sorted(zip(p,lst))]
