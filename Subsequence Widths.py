"""
Subsequence Widths

We can sort, since subsequences don't care about contiguity.

Then we iterate over each number - we subtract our answers by the number of times the current number is the minimum of a subsequence and add it the number of times it is the maximum of a subsequence.

To get the number of possible subsequence with n as the min or max, we count the number of number to its right (or left for max). For each number, there is 2 possible states - either we take it or not. So each number will double the number of possibilities, hence the powers_of_two[r].
"""
MOD = (10 ** 9) + 7
class Solution:
    def solve(self, nums):
        if len(nums) < 2: return 0
        powers_of_two = [0 for _ in nums]
        powers_of_two[0] = 1
        for i in range(1,len(powers_of_two)):
            powers_of_two[i] = powers_of_two[i-1]*2 % MOD
        ans=0
        nums.sort()
        for i,n in enumerate(nums):
            r=i
            l=len(nums)-i-1
            ans+=n * powers_of_two[r]
            ans-=n * powers_of_two[l]
        return ans % MOD