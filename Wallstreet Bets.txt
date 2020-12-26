"""
Wallstreet Bets

We can keep a monotonic decreasing queue, so that we can check every previous price smaller than the current one by popping of the end of the queue as long as values are smaller than the current one.

O(n) time, O(n) space. Beat that!
"""
class Solution:
    def solve(self, prices):
        ans=[0 for _ in prices]
        q=[]
        for i,p in enumerate(prices):
            while q and p > q[-1][1]:
                j=q[-1][0]
                ans[j] = i-j
                q.pop()
            q.append((i,p))
        return ans