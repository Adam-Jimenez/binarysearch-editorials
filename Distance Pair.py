"""
Distance Pair

Alex's answer is more space-efficient, but this helps me to visualize the problem. 

The first step is to reduce the dimensionality of the problem: we can combine nums[i]+i into x and nums[j]-j into y, so now we only have to maximize the sum of x[i] + y[j], i<j.

From a position x[i], we can pick any y[j] where j>i, but we are only interested in the maximal y[j] where j is greater than i. So instead of containing every individual value, each index in y will hold the maximal value to the right of the position y[j].

So then, we can lookup the max y[j] for i<j in constant time, while iterating over every possible x[i].
"""
class Solution:
    def solve(self, nums):
        x=[i+nums[i] for i in range(len(nums))]
        y=[nums[j]-j for j in range(len(nums))]
        for i in range(len(y)-2,-1,-1):
            y[i] = max(y[i], y[i+1])
        a=0
        for i in range(len(x)-1):
            a=max(a,x[i]+y[i+1])
        return a
            
                
