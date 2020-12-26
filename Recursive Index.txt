"""
Recursive Index

We apply A[k] while possible, incrementing the answer each time. We also delete the values behind our path, and if we encounter a deleted value we have detected a cycle.
"""
class Solution:
    def solve(self, A, k):
        ans=0
        while k>=0 and k<len(A):
            if A[k] is None: return -1
            A[k],k=None,A[k]
            ans+=1
        return ans
