"""
Longest Sublist with K Distinct Numbers

Sliding window solution: we iterate over the string and whenever the constraint is not respected, we know that there's no reason to keep going forward so we start popping characters from the left until the constraints are respected again.
"""
from collections import Counter
class Solution:
    def solve(self, k, s):
        start=0
        distinct=Counter()
        ans=0
        for i,c in enumerate(s):
            distinct[c]+=1
            while len(distinct)>k:
                old=s[start]
                distinct[old]-=1
                if distinct[old] == 0: 
                    del distinct[old]
                start+=1
            ans=max(ans, i-start+1)
        return ans
