"""
Bunnyhopping

Here, we have a dp array where we store the minimum cost to reach the end from any position. We start from the end, where we know that the minimal cost to reach the end is the cost of the end itself.

Then, we iterate backwards to the start. For each position, we set its value to the sum of the cost of reaching the position + the minimum cost in the window of size k following the position.

To keep track of the minimum cost in range k following the position, we use a monotone increasing queue, that keeps the values ordered and within range using some magic. First, it removes all indexes out of range, computes the current value, then appends the current value to the queue, removing all values greater or equal than it from the end.
"""
class Solution:
    def solve(self, nums, k):
        dp = [0 for _ in nums]
        dp[-1] = nums[-1]
        q=[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            while q and i+k < q[0]:
                q.pop(0)
            dp[i] = dp[q[0]]+nums[i]
            while q and dp[q[-1]] >= dp[i]:
                q.pop()
            q.append(i)
        return dp[0]
