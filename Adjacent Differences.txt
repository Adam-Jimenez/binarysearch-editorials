"""
Adjacent Differences

Take any increasing array: [1,4,8,9,10]
If we remove any number not touching the sides (e.g. 8), the max interval can only increase (4->8 will become 4->9), because the new difference between the hole made by removing the number will add together. So the strategy to minimize difference is removing numbers from the edges. We can use dp for this, as shown above. 
"""
from functools import lru_cache
class Solution:
    def solve(self, nums, k):
        diffs=[nums[i]-nums[i-1] for i in range(1,len(nums))]
        @lru_cache(None)
        def dp(i,j,cnt):
            if cnt==0: 
                m=0
                for k in range(i,j+1):
                    m=max(m,diffs[k])
                return m
            return min(dp(i+1,j,cnt-1), dp(i,j-1,cnt-1))
        return dp(0,len(diffs)-1, k)
        
