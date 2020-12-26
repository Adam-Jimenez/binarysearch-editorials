"""
Range Update

We want to avoid doing operations multiple times on the same indices. To do that, we can merge the operations with the following trick: 

Create a new list of events, modifying a running count. For the start of a range, we increment the counter and for the end, we decrement. This way, we only have to touch each number once. 
"""
class Solution:
    def solve(self, nums, operations):
        events=[]
        for l,r,inc in operations:
            events.append((l,inc))
            events.append((r+1,-inc))
        events.sort()
        inc=0
        ptr=0
        for i in range(len(nums)):
            while ptr<len(events) and events[ptr][0] == i:
                inc+=events[ptr][1]
                ptr+=1
            nums[i]+=inc
        return nums