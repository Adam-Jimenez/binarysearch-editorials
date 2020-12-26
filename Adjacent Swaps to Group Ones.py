"""
Adjacent Swaps to Group Ones

For each zero in our string, we count the number of ones to the left of it and to the right of it. For any zero, we know that it will have to swap either to the left or to the right of all those ones, so ideally we will swap with the least amount out of the two options. So the answer will be the sum of the minimal number of ones each zero has to swap with.
"""
class Solution:
    def solve(self, s):
        l,r=[0 for _ in s], [0 for _ in s]
        for i in range(1,len(s)): l[i]=l[i-1] + int(s[i-1]=="1")
        for i in range(len(s)-2,-1,-1): r[i]=r[i+1] + int(s[i+1]=="1")
        return sum(min(l[i], r[i]) for i in range(len(s)) if s[i]=="0")
