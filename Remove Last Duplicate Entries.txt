"""
Remove Last Duplicate Entries

We count frequencies, and store all duplicates in a set by checking if frequency is > 1.

Then we iterate over nums, decreasing frequency of each number met, and when we reach the last instance of a duplicate number we ignore it.
"""
from collections import Counter
class Solution:
    def solve(self, nums):
        c=Counter(nums)
        dup={x for x,f in c.items() if f>1}
        ans=[]
        for n in nums:
            if c[n]!=1 or n not in dup:
                ans.append(n)
                c[n]-=1
        return ans