"""
Minimum Set of Pairs

O(n^2 log (n^2)) solution. 

First, we generate a list with all the distances between all possible pairs: n^2 time.
Then, We sort the list based on the distance between the numbers in the pairs. We want to minimize the difference of the difference because we are free to choose the sign of the difference: 

imagine in the original list [2,3,4,6,9] we have the pair of numbers (2,4) with difference of two. If we want the difference to be -2, we put 4 in the first pair, and 2 in the second pair. If we want the difference to be 2, we put 4 in the first pair and 2 in the second pair.

So when we have our two pairs (2,4) and (3,6) with respective difference of 2 and 3, since we can rearrange the sign as we want we can get the minimal difference of sum by doing abs(diff1-diff2). 
abs(2-3) = abs(-1) = 1.

In the code, we sort the differences so we only have to check the neighboring pairs that don't contain the same numbers, and since the list is ordered we know which value is bigger, so we don't have to use abs.
"""
class Solution:
    def solve(self, nums):
        dists=[]
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                dists.append((abs(nums[i]-nums[j]), i, j))
        dists.sort()
        ans=1e9
        for i in range(len(dists)-1):
            dist,i1,i2 = dists[i]
            j=i+1
            dist2,i3,i4 = dists[j]
            while j<len(dists) and len({i1,i2,i3,i4})!=4:
                dist2,i3,i4 = dists[j]
                j+=1
            if len({i1,i2,i3,i4})==4:
                ans=min(ans, dist2-dist)
        return ans