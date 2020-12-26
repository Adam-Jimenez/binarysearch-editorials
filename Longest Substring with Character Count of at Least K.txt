"""
Longest Substring with Character Count of at Least K

Instead of trying to build an optimal solution, we can try taking the full string, and cutting it where the characters are of unsufficient frequency. Using a counter, we can iterate over the string, and if the frequency of the current character is less than k, we can recursively try to solve on the left part.

When all characters in the substring are of sufficient frequency, we can return the length of the current string.
"""
from collections import Counter
class Solution:
    def solve(self, s, k):
        def rc(lst):
            c=Counter(lst)
            acc=[]
            ans=0
            valid=True
            for x in lst:
                if c[x]<k:
                    valid=False
                    ans=max(ans,rc(acc))
                    acc=[]
                else:
                    acc.append(x)
            
            if valid:
                return len(acc)
            else:
                ans=max(ans,rc(acc))
                return ans
        return rc(list(s))