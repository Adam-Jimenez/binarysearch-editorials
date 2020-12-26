"""
Minimum Number of Flips to Have Alternating Values

We could repeat the input string twice, and use a sliding window using the size of the original string. 

To find the cost of the current string, we looked at the cost of first character in the window. If it is 1, the expected optimal string is 101010101 and so on, to avoid any cost. It if starts by 0, the expected string is 01010101..., so if we xor the current bit with the expected one we can get the current cost.

Now what happens when we shift our window? If the new starting bit is the same as the old one, it means the optimal string is shifted so we need to inverse the cost by doing k-cost-1. -1, because the start is no longer counted, and inverted because every wrong bit is now a correct one, and every correct one becomes wrong. If the new starting bit is not the same as the old starting bit, the optimal string is not changed, because 010101... shifted by one to the left is 101010...

When we add a bit, we compare it to the start. If the offset from the start is even, it means the current bit must be equal, otherwise they must be different.

O(n) time
O(n) space
"""
class Solution:
    def solve(self, s):
        k=len(s)
        s=s+s
        start=0
        cost=0
        ans=1e9
        for i in range(len(s)):
            if i-start>=k:
                ans=min(ans,cost)
                start+=1
                if s[start]==s[start-1]:
                    cost=k-cost-1
            offset=i-start
            if offset&1:
                if s[i]==s[start]:
                    cost+=1
            else:
                if s[i]!=s[start]:
                    cost+=1
        ans=min(ans,cost)
        return ans
