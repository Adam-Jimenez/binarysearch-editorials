"""
Next Integer Permutation

my implementation sucks, but the logic is the following:

You iterate on the number from the right, finding the first digit that has a bigger digit than itself to its right.

Then, you find the smallest digit to its right that is bigger than it, you swap them and sort everything to its right.
"""
class Solution:
    def solve(self, num):
        mx=0
        s=str(num)
        idx=-1
        ref=-1
        for i in range(len(s)-1,-1,-1):
            n=int(s[i])
            if n < mx:
                idx=i
                ref=n
                break
            elif n > mx: mx = n
        mn=1e9
        nidx=-1
        for i in range(idx+1, len(s)):
            n=int(s[i])
            if n > ref and n < mn: 
                mn = n
                nidx = i
        s = [c for c in s]
        s[idx],s[nidx] = s[nidx], s[idx]
        s = s[:idx+1] + sorted(s[idx+1:])
        ans= int("".join(s))
        if ans == num: return int("".join(sorted(s,key=int)))
        return ans
            
