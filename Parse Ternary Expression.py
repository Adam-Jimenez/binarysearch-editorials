"""
Parse Ternary Expression

We recursively try to solve until we reach a "true" or a "false". We find the left part by matching the first ?, and the right part by counting the number of ? and : until they balance out to 0.
"""
class Solution:
    def solve(self, s):
        s=s.strip()
        if s=="true": return True
        elif s=="false": return False
        l=s.index("?")
        r=matching(l,s)
        if self.solve(s[:l]):
            return self.solve(s[l+1:r])
        else:
            return self.solve(s[r+1:])
    
def matching(i,s):
    cnt=0
    while i<len(s):
        if s[i]=="?": cnt+=1
        elif s[i]==":": cnt-=1
        if cnt==0: return i
        i+=1