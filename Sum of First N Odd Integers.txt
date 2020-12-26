"""
Sum of First N Odd Integers

The sum of the first n odd numbers is n^2. We can demonstrate this by finding the average value of this arithmetic series and multiplying it n times. The average value times the number of values will give the sum.

The first element of the series is 1, and the nth element is 2(n-1)+1. 
So, the average value will be:
```
(1+2(n-1)+1)/2
(1+2n-2+1)/2
2n/2
n
```
We multiply it by n (the number  of values in the series) and we get n^2.
"""
class Solution:
    def solve(self, n):
        return n*n