"""
Maximum Sum Removing K Numbers From Ends

We store prefix sum and suffix sum, then try all possibilities of taking i from left and k-i from right.
"""
class Solution:
    def solve(self, nums, k):
        ps=[0]
        ss=[0]
        ans=0
        for n in nums:
            ps.append(ps[-1]+n)
        for i in range(len(nums)-1,-1,-1):
            ss.append(ss[-1]+nums[i])
        for i in range(k+1):
            ans=max(ans, ps[i]+ss[k-i])
        return ans