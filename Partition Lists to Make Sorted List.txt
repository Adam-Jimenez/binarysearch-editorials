"""
Partition Lists to Make Sorted List

We store the position of the numbers when they are sorted in a dictionary of queues. Then, we iterate of the numbers and create intervals between their original position and their sorted position. If we want the final array to be sorted, we know that we have to sort the range including the original position of the number and its sorted target position.

Then we can apply a regular overlapping intervals merging algorithm. The answer is the remaining count of non-overlapping intervals.

Note: Dealing with duplicates is particularly tricky, and is the reason I am using a deque for each position. For each leftmost occurrence of the number, we use the leftmost position in the sorted array to minimize potential overlap. 

O(N log N) time
O(n) space
"""
from collections import defaultdict, deque
class Solution:
    def solve(self, nums):
        sorted_pos=defaultdict(deque)
        for i,n in enumerate(sorted(nums)):
            sorted_pos[n].append(i)
        intervals=[]
        for i,n in enumerate(nums):
            x = sorted_pos[n].popleft()
            if i<x:
                a,b=i,x
            else:
                a,b=x,i
            intervals.append([a,b])
        stk=[]
        for s,e in intervals:
            if not stk or s>stk[-1][1]:
                stk.append([s,e])
            else:
                stk[-1][1]=max(stk[-1][1],e)
        return len(stk)
            