"""
Concatenated Sums

For each number, let's consider the number of times it will be at the bottom part of the concatenation. Since it will be the bottom for every number in the array, we can add the number times the length of the array to clear that part.

Now, let's consider how many times the current number is the top part of the concatenation. Since its value varies in function of the length of the bottom part, we can make a Counter of the lengths of each number, as to have buckets for each length with their associated frequency. 

Since a 32-bit integer has at most 2 billion as a value, we know that the length of the number is at most 10, so our algorithm stays linear. We iterate over each length, then consider how it shifts the current number: 10^(len) * num will give us the value of the top part.

Time: O(n)
Space: O(1), the counter will have at most 10 entries for same reason as explained above.

"""
from collections import Counter
class Solution:
    def solve(self, nums):
        cnt=Counter([len(str(n)) for n in nums])
        ans=0
        for i,n in enumerate(nums):
            ans+=n*len(nums) #bottom
            # top
            for l,freq in cnt.items():
                ans+=freq*(n*10**l)
        return ans
