"""
Upside Down Numbers

There is always one possible second half of the string, and it is determined by the first half, flipped over. We hardcode the mappings, and handle the middle differently to exclude "6" and "9"s.
"""
from itertools import product
mapping={
    "0":"0",
    "1":"1",
    "6":"9",
    "8":"8",
    "9":"6"
}
mids=["0","1","8"]
class Solution:
    def solve(self, n):
        if not n: return []
        ans=[]
        for half in product(mapping.keys(),repeat=n//2):
            half="".join(half)
            if half and half[0] == "0": continue
            rh=""
            for c in half:
                rh = mapping[c] + rh
            if n&1: # add middles
                for mid in mids:
                    ans.append(half+mid+rh)
            else:
                ans.append(half+rh)
        return ans
        
