"""
Make Lists Same with Sublist Sum Operations

Two pointers solution: We start with a pointer pointing at the start of each list, and a running sum for each list. We add the current numbers to the running sum, and increment the pointer with the smallest running sum, in the hopes that it will grow to become the running sum of the second list. When each running sum are equal, we have found an element in our resulting array. We can increment our answer and reset our running sums to zero.

To check if a solution is possible, we must reach the end of both lists with no running sum.
"""
class Solution:
    def solve(self, l0, l1):
        ans=i=j=a=b=0
        while True:
            if a != 0 and a == b:
                ans += 1
                a=b=0
            elif a < b:
                if i>=len(l0): break
                a += l0[i]
                i +=1
            else:
                if j>=len(l1): break
                b += l1[j]
                j += 1
        return ans if i == len(l0) and j == len(l1) and a == 0 and b == 0 else -1
