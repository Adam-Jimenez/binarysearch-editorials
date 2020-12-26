"""
Non-Overlapping Pairs of Sublists

We group valid chunks of number together using the groupby function.

Then, to pick our two sublists as stated in the problem, we have two possibilities:
- We can pick a sublist from a previous chunk
- We can pick a sublist from the current chunk

The first case is the simplest to handle. We can accumulate the number of possible sublists to the left of the current one with the formula n * (n+1) // 2, where n is the length of a chunk. For example, for a chunk of length 5, we have 1 sublist of length 5, 2 sublists of length 4, 3 sublists of length 3, and so on. The result is the arithemic series 1 + 2 + 3 + ... + n which equals n * (n+1) // 2. Then we take the product of the number of possibilities for the current chunk times the number of possible chunks to the left.

For the second case, we iterate over every split point in our chunk, so for a chunk of length 5, we can split it in the following ways : (1,4), (2,3), (3,2), (4,1). We compute the number of possibilities for the left and right part and take the product. We must also remove some overlap in the left part, because all the possibilities of length 1 are a subset of the possibilities of sublists of length 2. 
"""
from itertools import groupby
MOD = 10 **9 + 7
class Solution:
    def solve(self, nums, k):
        def sublist_cnt(n):
            return n * (n+1) // 2
            
        grps = []
        for valid, grp in groupby(nums, key=lambda x: x>=k):
            if valid:
                grps.append(len(list(grp)))
                
        left = 0
        ans = 0
        for n in grps:
            sc = sublist_cnt(n)
            ans = (ans + (left * sc)) % MOD
            for i in range(1,n):
                right = n - i
                ans += (sublist_cnt(i) - sublist_cnt(i-1)) * sublist_cnt(right) % MOD
            left += sc
        return ans % MOD