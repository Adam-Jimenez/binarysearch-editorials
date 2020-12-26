"""
K Distinct Window

We keep track of the distinct values in the window using a Counter. We increment the frequency of a number when it enters the window and decrement it as it leaves, appending the number of distinct numbers to our answer each time.
"""
from collections import Counter
class Solution:
    def solve(self, nums, k):
        c=Counter()
        for i in range(k):
            c[nums[i]]+=1
        ans=[]
        for i in range(k,len(nums)):
            ans.append(len(c))
            c[nums[i]]+=1
            c[nums[i-k]]-=1
            if c[nums[i-k]]==0: del c[nums[i-k]]
        ans.append(len(c))
        return ans
