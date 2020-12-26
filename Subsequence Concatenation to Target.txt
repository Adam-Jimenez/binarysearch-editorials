"""
Subsequence Concatenation to Target

The first step is checking if the problem is solvable. The only constraint we need to respect is that every character from target is in source. A single character is a valid sub sequence, so it makes it possible to solve it as so.

Then to solve the problem, we can use a common pattern that comes up in some subsequence pattern: for every position in source, we store the position of the next closest occurence of any character. This way, we can jump to it in constant time.

After, we iterate over the target. For each character, we ask: "What is the closest right occurence of this character?". If it doesn't show up to the right of the current position, we need to start a new subsequence starting from index 0.

O(n) time but with high coefficient because of the creation of n dictionaries with at most 26 elements.
O(n) space, for storing the dictionaries.
"""
class Solution:
    def solve(self, source, target):
        a=set(source)
        b=set(target)
        if a&b < b: 
            return -1
        nxt=[None for _ in source]
        nxt[-1]={}
        for i in range(len(source)-1,-1,-1):
            if i < len(source)-1:
                nxt[i]=nxt[i+1].copy()
            nxt[i][source[i]]=i
        ans=1
        i=0
        j=0
        while j < len(target):
            if i == len(source):
                i=0
                ans+=1
            c=target[j]
            if c not in nxt[i]:
                ans+=1
                i=0
            i=nxt[i][target[j]]+1
            j+=1
        return ans
            
