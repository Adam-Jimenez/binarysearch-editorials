"""
List Consecutive Split

The logic is to compute the frequency of each number, then take the smallest k numbers, check if they are continuously increasing and remove them.
"""
from collections import Counter
class Solution:
    def solve(self, nums, k):
        c=Counter(nums)
        while len(c)>=k:
            sub=sorted(c.keys())[:k]
            if any(sub[i]!=sub[i-1]+1 for i in range(1,len(sub))): return False
            for key in sub:
                c[key]-=1
                if not c[key]: del c[key]
        return len(c)==0
