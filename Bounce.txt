"""
Bounce

For each position, try going both left and right recursively. Keep note of visited positions to avoid going into a cycle. If we reach the final position, return True.
"""
class Solution:
    def solve(self, nums, k):
        seen=set()
        def dfs(pos):
            if pos in seen: return False
            if pos == len(nums)-1: return True
            seen.add(pos)
            if 0<=pos<len(nums):
                if dfs(pos+nums[pos]): return True
                if dfs(pos-nums[pos]): return True
            return False
        return dfs(k)
