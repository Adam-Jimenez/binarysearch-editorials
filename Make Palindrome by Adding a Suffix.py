"""
Make Palindrome by Adding a Suffix

We try to find the largest palindrome that touches the right border, and the answer consist in the number of characters not included in that palindrome.
"""
class Solution:
    def solve(self, s):
        ans=len(s)-1
        for i in range(len(s)):
            for j,k in ((i,i), (i,i+1)):
                l,r= expand(j,k,s)
                if r==len(s)-1:
                    ans=min(ans,len(s)-(r-l+1))
        return ans
        
def expand(i,j,s):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    i+=1
    j-=1
    return i,j