"""
List Equality with Increments

The strategy used here is for for each iteration, we take the max and the min, and increment until the min is equal to the max. For example:
```
[1,2,3,4]
```
We have 4 as max, and 1 as min. We increment every number by (4-1) except 4:
```
[4,5,6,4]
```
We now have two equal numbers, and our problem is reduced. We repeat the process with max (6) and min(4):
```
[6,7,6,6]
```
And again with 7 and 6:
```
[7,7,7,7]
```
For each step, we can notice that __the difference between any number and the min never changes__, until we select it and equalize with the number, and then the cost will be xi-min.
In our example, the difference between 3 and 1 is 2, and when we increment the min, the difference between the same numbers (6 and 4) is still 2.
"""
class Solution:
    def solve(self, nums):
        mn=min(nums)
        return sum(x-mn for x in nums)