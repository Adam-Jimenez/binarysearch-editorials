"""
Lossy Run-Length Encoding

We apply a sliding window of size k on the substring we want to remove. To compute the cost (the length of the resulting run-length encoded string), we can take the cost of the prefix before the substring, and the suffix after the substring, and merging the interior part if the characters are the same.

To do this, I compute a prefix array that contains two informations: the cost of all previous characters and the length of the current run, so we can combine the lengths if the character ending the prefix or the character starting the suffix is the same.
"""
class Solution:
    def solve(self, s, k):
        def prefix(s):
            pre=[[0,0]] # [past_cost, current_run_length]
            last=None
            for c in s:
                if c == last:
                    pre.append([pre[-1][0], pre[-1][1]+1])
                else:
                    pre.append([pre[-1][0]+cost_fn(pre[-1][1]), 1])
                last=c
            return pre
        pre=prefix(s)
        suf=prefix(s[::-1])[::-1]
        ans=float('inf')
        for i in range(len(s)-k+1):
            j=i+k
            left,midl = pre[i]
            right,midr = suf[j]
            cost=left+right
            c1=s[i-1] if i>0 else None
            c2=s[j] if j<len(s) else None
            if c1 == c2:
                cost+=cost_fn(midl+midr)
            else:
                cost+=cost_fn(midl)+cost_fn(midr)
            ans=min(ans,cost)
        return ans
        
def cost_fn(l):
    if l == 0:
        return 0
    if l == 1:
        return 1
    else:
        return len(str(l))+1