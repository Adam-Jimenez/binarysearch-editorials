"""
Fractional Knapsack

We can greedily take knapsacks with the largest ratio of value per weight unit. When we reach a knapsack we can't take completely, we take the largest fraction possible.
"""
class Solution:
    def solve(self, weights, values, capacity):
        a=[(val/wei, wei, val) for wei, val in zip(weights,values)]
        a.sort(reverse=True)
        i=0
        ans=0
        while i<len(a) and capacity>0:
            ratio,weight,value = a[i]
            if weight<= capacity:
                capacity-=weight
                ans+=value
            else:
                ans+=(capacity/weight)*value
                capacity=0
            i+=1
        return int(ans)
