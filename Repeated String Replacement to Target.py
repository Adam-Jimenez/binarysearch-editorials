"""
Repeated String Replacement to Target

For the transformation to be possible there must be only one character mapped to each character, so the number of unique mappings must be equal to the number of unique characters in S. 

O(n) time
O(n) space
"""
class Solution:
    def solve(self, s, t):
        return len(set(s)) == len(set(zip(s,t)))
