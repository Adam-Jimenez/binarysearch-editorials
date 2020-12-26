"""
Number of Sublists With Sum of Target

We keep a running sum from all elements from 0 to i, and we increment the number of times we have seen this sum.

Each time we have a sum at an index, you can calculate the difference of the current sum with the target value.

If the running sum was equal to that difference at some point, you can remove that previous running sum from the current to make a sublist. 


"""
from collections import defaultdict
class Solution:
    def solve(self, nums, target):
        seen=defaultdict(int)
        seen[0]=1
        s=0
        ans=0
        for i in range(len(nums)):
            s+=nums[i]
            comp=s-target
            if comp in seen:
                ans+=seen[comp]
            seen[s]+=1
        return ans
