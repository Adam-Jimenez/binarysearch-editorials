"""
Last to Toggle Wins

Best explained here: https://cp-algorithms.com/game_theory/sprague-grundy-nim.html
"""
from functools import lru_cache
from itertools import groupby
class Solution:
    def solve(self, nums):
        ans=0
        for k,grp in groupby(nums):
            if k: ans^=grundy(len(list(grp)))
        return ans>0
        
def mex(seen):
    a=0
    while a in seen:
        a+=1
    return a

@lru_cache(None)
def grundy(n):
    if n <= 1: return 0
    seen={grundy(n-2-i)^grundy(i) for i in range(n-1)}
    return mex(seen)

