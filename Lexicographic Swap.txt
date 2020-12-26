"""
Lexicographic Swap

We want to minimize the values of the letters iterating from the left. If we could swap as much as we wanted, we would just sort the string but we can just swap once. So we can compare the string to its sorted equivalent and take the first value that doesn't match. We find its rightmost occurrence in the original string to minimize the value of the swap, and do the swap.
"""
class Solution:
    def solve(self, s):
        ss=sorted(s)
        for i,(c1,c2) in enumerate(zip(s,ss)):
            if c1 != c2: break
        j=s.rindex(ss[i])
        s = list(s)
        s[i],s[j]=s[j],s[i]
        return "".join(s)
                
