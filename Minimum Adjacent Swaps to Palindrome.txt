"""
Minimum Adjacent Swaps to Palindrome

The first step is to check for validity - we can make a palindrome only if there is at most 1 character of odd frequency (the center).

Then we can apply a two pointer solution, one pointer pointing the leftmost character and one pointer pointing the rightmost character. If they are equal, we can continue on to the next sub problem by incrementing/decrementing both pointers.

If they are unequal, we check the cost of swapping the rightmost occurence of the left character completely to the right versus swapping the leftmost occurence of the right character to the left - we can greedily take the minimum cost. I have no idea how to prove this, so this exercice will be left as an exercice to the reader :) (let me know if you know how to prove it).

One important case to handle as well is when we meet the character of odd frequency, the center. When we meet it, we are forced to swap it because it cannot stay on the edge of the current substring.
"""
from collections import Counter
class Solution:
    def solve(self, s):
        cnt=Counter(s)
        if sum(1 for freq in cnt.values() if freq&1)>1: return -1
        s=list(s)
        i=0
        j=len(s)-1
        def swap(start,end, step=1):
            first=s[start]
            for i in range(start,end,step):
                s[i] = s[i+step]
            s[end]=first
        ans=0
        while i<j:
            leftchar = s[i]
            rightchar = s[j]
            if leftchar != rightchar:
                rightmostleft = "".join(s).rindex(leftchar,i,j)
                leftmostright = s.index(rightchar,i,j)
                # checking for middle
                if cnt[leftchar]&1:
                    swap(leftmostright, i, -1)
                    ans+=leftmostright-i
                elif cnt[rightchar]&1:
                    swap(rightmostleft, j)
                    ans+=j-rightmostleft
                elif leftmostright < (len(s)-1-rightmostleft):
                    swap(leftmostright, i, -1)
                    ans+=leftmostright-i
                else:
                    swap(rightmostleft, j)
                    ans+=j-rightmostleft
            i+=1
            j-=1
        return ans
