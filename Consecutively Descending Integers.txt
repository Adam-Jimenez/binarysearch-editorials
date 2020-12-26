"""
Consecutively Descending Integers

Brute-force all initial number lengths. For each number, we check if its equal to the previous one minus one, and then we jump to the next number. If the current number is a power of ten, we need to reduce the size of the next number by one (except for one and zero).
"""
from math import log
class Solution:
    def solve(self, s):
        def dfs(i,j,prev):
            if i>=len(s): return True
            cur=s[i:j]
            cur_num=int(cur)
            if prev is not None and cur_num != prev-1: return False
            ni = j
            nj = ni+len(cur)
            if cur_num not in (1,0) and log(cur_num,10).is_integer():
                nj-=1
            return dfs(ni,nj, int(cur))
        for j in range(1, (len(s)+2)//2):
            if dfs(0,j,None): return True
        return False
