"""
Longest Zero Sublist Sum

We can find intervals where the sum is zero by the running sum is equal for two indexes, which means the difference in sum between the two points is zero.
"""
class Solution:
    def solve(self, nums):
        d={0:-1}
        ans=0
        sm=0
        for i,n in enumerate(nums):
            sm+=n
            if sm in d:
                ans=max(ans, i-d[sm])
            else:
                d[sm] = i
        return ans
            
