"""
Unique Characters of Every Substring

We build a dictionary of lists that contains the indexes of each unique character. 

Let's say we have a string a__a__a where _ is any character except a. The number of times the middle a is adding 1 to the answer is the number of substrings where it is the only a. To count that, we can multiply the number of possible left bounds of substrings to the number of possible right bounds. The possible left bounds are all the values between the previous a and the current index, and the possible right bounds are all the values between the next a and the current index.
"""
from collections import defaultdict
class Solution:
    def solve(self, s):
        pos=defaultdict(list)
        for i,c in enumerate(s):
            pos[c].append(i)
        ans=0
        for lst in pos.values():
            for i,idx in enumerate(lst):
                prev = -1 if i == 0 else lst[i-1]
                next = len(s) if i == len(lst)-1 else lst[i+1]
                left = next-idx
                right= idx-prev
                ans += left * right
        return ans % (10 ** 9 + 7)
