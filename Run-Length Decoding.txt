"""
Run-Length Decoding

Group digits together and letters together.

Each time you see a group of letters, repeat it by the last number seen.
"""
from itertools import groupby
class Solution:
    def solve(self, s):
        cnt=1
        ans=""
        for k,grp in groupby(s, key=lambda x: x.isdigit()):
            if k:
                cnt = int("".join(grp))
            else:
                ans+=cnt*str("".join(grp))
                cnt=1
        return ans
        
