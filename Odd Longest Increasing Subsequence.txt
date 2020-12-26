"""
Odd Longest Increasing Subsequence

The best way to approach this problem is to build on top of sub-problems, starting with the first number in the array, then the second, etc. 

Let's take [10,12,14,3,5,6] for example. First, we consider the sub-problem [10]: what is the longest increasing sequence? Since we only have one number, the answer is one. We also need to keep track of the number of odd numbers, which we can do using a dictionary where the key is the number of odd numbers and the value is the longest increasing sequence. So in this case we will have {0: 1}.

Then for [10,12], we will have [{0:1}, {0:2}], because using 12, we can build on top of the longest increasing sub-sequence of 10 since 12 > 10, but we still have 0 odd numbers.

For [10,12,14]: [{0:1}, {0:2}, {0:3}]
For [10,12,14,3]: [{0:1}, {0:2}, {0:3}, {1:1}]. Note that we can't use any of the previous sequences because three is smaller than all the previous values. 

For [10,12,14,3,4]: [{0:1}, {0:2}, {0:3}, {1:1}, {1:2}]
Finally: [10,12,14,3,4,5]: [{0:1}, {0:2}, {0:3}, {1,1}, {1:2}, {2:3}]

Then we iterate over every dictionary and their keys, checking all the values where the number of odds is greater or equal to k. We take the maximum value.
"""
from collections import defaultdict
class Solution:
    def solve(self, nums, k):
        lens = [defaultdict(int) for _ in nums]
        for i,n in enumerate(nums):
            lens[i][n&1]+=1
            
        for i in range(len(nums)):
            is_odd = nums[i]&1
            for j in range(i):
                if nums[j]>=nums[i]:continue
                for odd_count,length in lens[j].items():
                    lens[i][odd_count+is_odd]=max(lens[i][odd_count+is_odd], length+1)
        ans=0                
        for d in lens:
            for odd_count,length in d.items():
                if odd_count>=k and length>ans: ans=length
        return ans
            
