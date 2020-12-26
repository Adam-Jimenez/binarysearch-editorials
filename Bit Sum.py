"""
Bit Sum

To minimize the sum, we want to flip the rightmost 0 bits. So we can iterate over the bits of every numbers, and then greedily takes the k rightmost bits.

I also cheesed it a bit by considering 32 bits for all numbers, and all bits left of the last one bit are also zeroes.
"""
from collections import defaultdict
class Solution:
    def solve(self, nums, k):
        bitcount = defaultdict(int)
        for n in nums:
            b = bin(n)[2:]
            for i,bit in enumerate(b[::-1]):
                if bit == "0": bitcount[i]+=1
            for j in range(i+1, 32):
                bitcount[j]+=1
        s=sum(nums)
        p = sorted(bitcount.items())
        while k > 0:
            bit,cnt = p.pop(0)
            n = min(k,cnt)
            s += n * 2**bit
            k-=n
        return s % (10 ** 9 + 7)
