"""
String Expansion

Each time we see a number, we add it to our coefficient variable.

Each time we see an opening parenthesis, we find the matching one and solve recursively.

Otherwise we just accumulate characters.
"""
class Solution:
    def solve(self, s):
        ans=""
        coeff=""
        i=0
        while i<len(s):
            c=s[i]
            if c.isdigit():
                coeff+=c
            elif c == "(":
                j=matching(s,i)
                ans+=int(coeff) * self.solve(s[i+1:j])
                coeff=""
                i=j
            else:
                ans+=c
            i+=1
        return ans
                
def matching(s,i):
    cnt=0
    while True:
        if s[i] == "(": cnt+=1
        elif s[i] == ")": cnt-=1
        if cnt==0: return i
        i+=1