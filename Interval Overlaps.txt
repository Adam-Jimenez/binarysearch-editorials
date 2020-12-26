"""
Interval Overlaps

Given two intervals:

There is an intersection if the maximum of their start is smaller or equal to the minimum of their ends. Example:
[---]   [--]
1--4  5--6
max(1,5)=5, min(4,6)=4, hi<lo => no intersection.
[---[--]--]
1--4--5--6
max(1,4)=4, min(5,6)= 5, 5>=4 => intersection from 4 to 5.

Given that the intervals are in sorted order, we can't increase our interval to the left, only to the right, so we discard our interval with the smallest end, since it is encapsulated by the one with the larger end.

https://leetcode.com/problems/interval-list-intersections/solution/


"""
class Solution:
    def solve(self, A, B):
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
