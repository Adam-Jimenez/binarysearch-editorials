"""
Partition String

We find the leftmost occurence and the rightmost occurence for each character.

Then, we consider the range between the leftmost and rightmost occurence of a character an interval. We reduce the problem to the merging overlapping intervals problem.

We do not need to sort the intervals, since i add the intervals in the intervals array according to their order in the string - where they are already ordered.

O(n) time, O(n) space
"""
class Solution:
    def solve(self, s):
        left={}
        right={}
        for i,c in enumerate(s):
            if c not in left:
                left[c]=i
            right[c]=i
        intervals=[]
        seen=set()
        for c in s:
            if c not in seen:
                seen.add(c)
                intervals.append([left[c],right[c]])
        stk=[]
        for start,e in intervals:
            if not stk or start>stk[-1][1]:
                stk.append([start,e])
            else:
                stk[-1][1]=max(e,stk[-1][1])
        ans=[]
        for start,e in stk:
            ans.append(e-start+1)
        return ans