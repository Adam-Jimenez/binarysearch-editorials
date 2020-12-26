"""
Majority Vote

Constant space solution using Boyer-Moore majority vote algorithm: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
"""
class Solution:
    def solve(self, nums):
        el=cnt=0
        for n in nums:
            if cnt==0: 
                el=n
                cnt=1
            elif n==el: cnt+=1
            else: cnt-=1
        cnt=sum(1 for n in nums if n==el)
        return el if cnt>(len(nums)//2) else -1
        