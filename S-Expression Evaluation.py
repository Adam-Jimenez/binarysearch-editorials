"""
S-Expression Evaluation

Recursive approach:

- Each time we a parentheses, we find the matching one and evaluate recursively.
- Otherwise, we group our three values into an array and evaluate them.
"""
class Solution:
    def solve(self, s):
        ans=[""]
        i=1
        while i<len(s)-1:
            if s[i]=="(":
                j=matching_paren(s,i)
                ans[-1]+=str(self.solve(s[i:j+1]))
                i=j
            elif s[i]==" " and ans[-1]:
                ans.append("")
            else:
                ans[-1]+=s[i]
            i+=1
        return compute(*ans)
        
def compute(op,x,y):
    d={
        "+": lambda x,y: x+y,
        "-": lambda x,y: x-y,
        "*": lambda x,y: x*y,
        "/": lambda x,y: int(x/y)
    }
    print(op,x,y)
    return d[op](int(x),int(y))
    
def matching_paren(s, i):
    paren=0
    for j in range(i, len(s)):
        if s[j]=="(":paren+=1
        elif s[j]==")":paren-=1
        if not paren: return j