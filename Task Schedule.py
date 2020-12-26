"""
Task Schedule

We greedily take the k+1 most common task, that represent the number of tasks you must do before being able to redo the first one.

When the number of unique tasks gets smaller than k, we continue adding k+1 time each iteration, but only subtract one from the available tasks.

We avoid waiting at the end by checking if there's anything left in the dictionary. If not, we just add the number of tasks left in the last iteration.
"""
from collections import Counter
class Solution:
    def solve(self, nums, k):
        c=Counter(nums)
        ans=0
        while c:
            common=c.most_common(k+1)
            for task,freq in common:
                c[task]-=1
                if c[task]==0: del c[task]
            ans+=k+1 if c else len(common)
        return ans
