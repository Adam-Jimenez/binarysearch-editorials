"""
Equalize List

Two methods to solve this problem: one using binary search to find the minimum of the cost function, and the second using a median.

Explained here: https://www.youtube.com/watch?v=LR2AsgCoPGc
"""
class Solution: 
    def solve(self, nums, costs):
        return self.solve_math(nums, costs)
        
    def cost_fn(self, nums, costs, target):
        total_cost=0
        for i,n in enumerate(nums):
            dist=abs(target-n)
            total_cost += dist * costs[i]   
        return total_cost
        
    def solve_math(self, nums, costs):
        a = sorted(zip(nums,costs))
        median_pos = sum(costs)//2
        for n, cost in a:
            if cost > median_pos: return self.cost_fn(nums,costs,n)
            median_pos -= cost
        return self.cost_fn(nums,costs,n)
    
    def solve_binarysearch(self, nums, costs):
        def find_peak():
            lo=0
            hi=max(nums)
            while lo<hi:
                mid = (lo+hi)//2
                if self.cost_fn(nums,costs,mid)>self.cost_fn(nums,costs,mid+1):
                    lo=mid+1
                else:
                    hi=mid
            return lo
        t= find_peak()
        return self.cost_fn(nums,costs,t)
                    
            
                
