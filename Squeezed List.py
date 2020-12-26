"""
Squeezed List

Alternative syntax I learned about today. Using:

```python
head,*body,tail=nums
```
You can use easily extract the first and last value of the nums. If nums is of length two, the body will be empty so we can replace it by a 0.
"""
class Solution:
    def solve(self, nums):
        ans=[nums[::]]
        while len(nums)>1:
            head,*nums,tail=nums
            nums=nums or [0]
            nums[0]+=head
            nums[-1]+=tail
            ans.append(nums[::])
        return ans
