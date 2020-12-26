"""
Symmetric Blocks

This was a tough one. Even though I managed to solve it during the contest, I felt like I needed to come back to it with a fresh perspective to come up with a logical solution. Here it finally is (hopefully)!

The hardest part of this problem is understanding the relation between the height, and the position (j) of the block. We can take a simple example to illustrate it:
```
X
X
XXX
```
Here, We can see that the height of the first block is equal to the length of the array. Let's try another example:
```
XX
XX
XXXX
XXXX
```
We can see again that the first block is the same length as the array. But let's look at how the height of the rightmost element affects the symmetry. Since the last block is of height 2, it tells us that the first 2 elements must be of height n, the length of the array. 

We can generalize this for any position in the array. For any position j, its height tells us how many elements counting from the left must be at least of height j. If we iterate from the right, we can assert that those elements must be exactly height j, because every j to the left will be smaller.
"""
class Solution:
    def solve(self, nums):
        i=0
        j=len(nums)-1
        while i<=j:
            h=nums[j]
            while i<h:
                if nums[i] != j+1: return False
                i+=1
            j -= 1
        return True
