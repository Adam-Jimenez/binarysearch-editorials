"""
Embolden

We can use regex to find all overlapping matches of each pattern: https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring

We store the length of the pattern, and the position at which it has been seen in a list. Then when iterating, we keep a decrementing counter, and when it reaches zero, we are no longer in a match.
"""
import re
class Solution:
    def solve(self, text, patterns):
        patterns=set(patterns)
        mark=[0 for _ in text]
        for p in patterns:
            l=len(p)
            for m in re.finditer(f"(?={p})",text):
                i = m.start()
                mark[i] = max(mark[i], l)
        ans=[]
        cnt=0
        for i,c in enumerate(text):
            new_cnt=max(mark[i],cnt-1)
            if not cnt and new_cnt: ans.append("<b>")
            elif cnt and not new_cnt: ans.append("</b>")
            ans.append(c)
            cnt=new_cnt
        if cnt: ans.append("</b>")
        return "".join(ans)