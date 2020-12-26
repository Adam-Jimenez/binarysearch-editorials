"""
Remove Sublist to Reach Equilibrium

We can build a prefix array and a suffix array, both counting the equilibrium before a given index and after a given index. Equilibrium is decremented when n<k and incremented when n>k. 

So, for a sublist removal to attain an equilibrium of 0, we need a sublist nums[i:j] where prefix[i] == -suffix[j], so that the prefix is the inverse of the suffix which makes them balance out.

To do this, we can iterate over every number, and mark its index in a dictionary. Then, we check if we have ever seen -n in the dictionary, if so, it means that we have a prefix that balances out with the current suffix. It is a potential answer, which we minimize to find the result. 

O(n) time
O(n) space
"""
class Solution:
    def solve(self, nums, k):
        if sum((n<k)*-1+(n>k)*1 for n in nums) == 0: return len(nums)
        def prefix(l):
            pf=[0]
            for n in l:
                inc=0
                if n>k: inc=1
                if n<k: inc=-1
                pf.append(pf[-1]+inc)
            pf.pop()
            return pf
        left=prefix(nums)
        right=prefix(nums[::-1])[::-1]
        seen={}
        ans=0
        for i in range(len(right)-1,-1,-1):
            seen[right[i]]=i
            n=left[i]
            if -n in seen:
                j=seen[-n]
                ans=max(ans,len(nums)-(j-i+1))
        return ans