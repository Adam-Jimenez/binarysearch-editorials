"""
Swapping Socks

One important note about this problem is that pairs can be unordered, so (1,0) and (0,1) are both valid pairs.

We iterate over the current pairs of the array. We look at the first sock in the pair, and compute the expected second pair by flipping the last bit, so the even pair will give the odd pair and vice-versa.

If the pairs don't match, find the index of the expected pair and greedily swap.
"""
class Solution:
    def solve(self, row):
        idx={v:i for i,v in enumerate(row)}
        ans=0
        for i in range(0,len(row), 2):
            first=row[i]
            second = first^1
            if row[i+1]!=second:
                j=idx[second]
                row[i+1],row[j]=row[j],row[i+1]
                idx[row[j]]=j
                ans+=1
        return ans