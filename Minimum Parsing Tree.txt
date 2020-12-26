"""
Minimum Parsing Tree

This is a recursive complete-search solution, that goes as follows:

We start with pointers (i,j) that represent the start and the end of the current interval.

[ 0, 5, 8, 9 ]

..^ i ....... ^ j

Then, we iterate over each position (k) between those two pointers. This will be the split position.

[ 0, 5, 8, 9 ]

..^i ^k.... ^j

For every split position (k), we make two recursive calls. Once for the left interval [i,k] and once for the right interval [k,j]. This represents potential children of the current node. In this example, the children are [0,5] and [5,9].

When we reach a position where the interval is of size 2 (when i & j are next to eachother):

[ 0, 5, 8, 9 ]

.^i ..^j

We compute the interval of the node with arr[j]-arr[i].

When we receive the value of the children, we pick the one with the minimum interval, we add the size of the current interval and return the result.

With the algorithm completed, we now need to add memoization, because there are many overlapping subproblems. For example:

[1,2,3,4,5,6]

Eventually we will need to compute the value [1,2], [1,3], [1,4] and [1,5]. When we compute [1,5], we will add the result of [1,4] and [4,5]. When we computer [1,4], we will add the result of [1,3] and [3,4], etc...

Python's functools package offers lru\_cache, that detects when a function was called with the exact same parameters, and returns the value that was computed by those parameters. It solves our problem of overlapping subproblems and we no longer have a time limit exceeded error.

Thanks for coming to my TED talk.

"""
from functools import lru_cache
class Solution:
    
    def solve(self, breakpoints):
        @lru_cache(None)
        def divide(i,j):
            if j == i+1:
                return breakpoints[j]-breakpoints[i]
            min=1e9
            for k in range(i+1, j):
                res=divide(i,k)+divide(k,j)
                if res < min:
                    min=res
            return min+breakpoints[j]-breakpoints[i]
        return divide(0,len(breakpoints)-1)
        # Write your code here
