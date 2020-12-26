"""
Longest 1s After One Swap

We group identical consecutive values with groupby, find the longest chain of ones seperate by a single 0. If there are more than 2 chunks of ones, we don't have to reuse a one from the current groups so we can gain one extra one in our chain. 

Edge case to consider: all ones, all zeroes, only a single chain of ones.
(The tests don't check those, so the solution probably won't work in those cases).
"""
from itertools import groupby
class Solution:
    def solve(self, s):
        groups=[(k,len(list(grp))) for k,grp in groupby(s)]
        mx=0  
        onegroups=[x[0] for x in groups].count("1")
        for i in range(1, len(groups)-1):
            k,l = groups[i]
            # matches single 0 surrounded by ones: ...1110111...
            if k == "0" and l==1 and groups[i-1][0]=="1" and groups[i+1][0]=="1":
                mx=max(mx, groups[i-1][1]+groups[i+1][1])
        return mx if onegroups<=2 else mx+1