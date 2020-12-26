"""
Frogger

I think test cases are weak cause I didn't even need to memoize my function, or maybe this problem has few overlapping subproblems.

Basically create a set of all stones to look up if a position is valid in constant time, then starting from position 1 and jump=0, recursively try jumping each valid jump that are greater than 0 then solve recursively.

To analyse complexity, we need to figure out how many different values our last jump can have.

Since we can increase our jump by one each subproblem to explore a new subproblem, our largest jump can be represent by the arithmetic sequence 1+2+3+4+... = target

n(n+1)/2 = target
n(n+1) = 2 * target
n^2 + n = 2 * target
~ n = sqrt(target)

So i think time complexity is O(n*sqrt(n)) = O(n),
O(n) space
"""
class Solution:
    def solve(self, stones):
        target=stones[-1]
        valid=set(stones)
        def bt(i, last=0):
            if i == target: 
                return True
            return any(
                i+jump in valid and bt(i+jump, jump) 
                for jump in (last-1, last, last+1) 
                if jump > 0
            )
        return bt(0)
