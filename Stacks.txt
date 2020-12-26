"""
Stacks

Since we can pop off any number of elements we want, we check all prefix sums as they all are possible solutions. Because the stack contains only positive values, we will never see the same sum twice for one stack.
"""
from collections import defaultdict
class Solution:
    def solve(self, stacks):
        sums=defaultdict(int)
        for stk in stacks:
            s=0
            for n in stk:
                s+=n
                sums[s]+=1
        ans=0
        for s,f in sums.items():
            if f >= len(stacks) and s > ans:
                ans=s
        return ans