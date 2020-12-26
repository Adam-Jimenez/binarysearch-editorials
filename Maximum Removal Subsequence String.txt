"""
Maximum Removal Subsequence String

We build the leftmost greedy subsequence and the rightmost greedy subsequence by iterating by both sides, greedily picking the characters out of our subsequence.

Then, we can either:
1. remove the substring to the left of our rightmost subsequence, 
2. remove the substring to the right of our leftmost subsequence,
3. remove the substring between the leftmost position for the current char and the rightmost position for the next char (which is included in a valid subsequence, as computed previously).

Totally not copied from lasa's solution ;) ;)
"""
class Solution:
    def solve(self, a, b):
        l=[]
        r=[]
        j=0
        for i,c in enumerate(a):
            if c==b[j]:
                l.append(i)
                j+=1
            if j == len(b): break
        j=len(b)-1
        for i in range(len(a)-1,-1,-1):
            c=a[i]
            if c == b[j]:
                r.append(i)
                j-=1
            if j == -1: break
        r=r[::-1]
        return max(r[0], len(a)-1-l[-1], *[r[i+1]-l[i]-1 for i in range(len(l)-1)])
