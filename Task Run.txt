"""
Task Run

We keep track of the last time we saw the current task type using a dictionary. 

When we see a task, we check if we already saw the current type by doing a dictionary lookup. If we didn't, we can just increase answer by one.

IF we already saw the task, we compute the distance between the current task and the old one. If its less than k we need to wait the difference. We offset the position i by the total waited time. 
"""
class Solution:
    def solve(self, tasks, k):
        last = {}
        ans = waited = 0
        for i, t in enumerate(tasks):
            if t not in last:
                ans += 1
            else:
                diff = i - last[t] + waited
                if diff <= k:
                    wait = k - diff + 1
                    waited += wait
                    ans += wait
                ans += 1
            last[t] = i + waited
        return ans