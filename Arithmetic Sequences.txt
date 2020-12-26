"""
Arithmetic Sequences

We create an array with the difference of contiguous elements. We group identical chunks of differences together, and we will get the length of the longest arithmetic series of a given difference. To compute the number of arithmetic series greater than 3 in length inside this arithmetic serie, we ironically have to use the arithmetic serie 1+2+...+n. Here's why:

Take: 3,5,7,9,11,12,13
Our differences will be [2,2,2,2,1,1]
We have 4 differences of 2, which means we have a serie of length (4+1).
With 5 elements, we can build one serie of length 5, two series of length 4 and 3 series of length 3. So we have 1+2+3. 

The value of 1+2+..+n is n(n+1)//2. We set n = l-1 and we are golden.
"""
from itertools import groupby
class Solution:
    def solve(self, nums):
        diff=[nums[i]-nums[i-1] for i in range(1,len(nums))]
        ans=0
        for _, grp in groupby(diff):
            l=len(list(grp))
            if l>1:  ans += l*(l-1)//2
        return ans
