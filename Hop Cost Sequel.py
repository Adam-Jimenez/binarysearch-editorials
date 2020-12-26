"""
Hop Cost Sequel

To find the optimal answer, we can treat this problem as a graph, where each node we can visit from the current one are i+1, i-1, and all nodes with same value.

Then, to find the minimum steps, we explore all nodes we can reach within 1 step, all nodes we can reach within 2 steps, etc. Otherwise known as BFS (breadth-first search).

So when we first encounter the last index of the array, we can return early, and if we meet an index that was already treated, we know that we cannot get a better answer by visiting it with a larger step count.

We can delete the strongly connected components composed of same values when we visit them, because we know we won't be able to get a better answer by revisiting the positions.

O(n) time because we visit each index once, O(n) space because we store all seen indexes.
"""
from collections import deque,defaultdict
class Solution:
    def solve(self, nums):
        val_idx = defaultdict(list)
        for i,x in enumerate(nums):
            val_idx[x].append(i)
        def get_neighbors(i):
            val=nums[i]
            if i>0:
                yield i-1
            if i < len(nums)-1:
                yield i+1
            for j in val_idx[val]:
                yield j
            del val_idx[val]
        seen=set()
        q=deque()
        seen.add(0)
        q.append(0)
        ans=0
        while q:
            for _ in range(len(q)):
                cur=q.popleft()
                if cur == len(nums)-1: return ans
                for nei in get_neighbors(cur):
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
            ans+=1
        return -1
            
