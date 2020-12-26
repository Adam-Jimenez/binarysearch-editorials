"""
First Missing Positive Sequel

The sum of the arithmetic series 1+2+3+...+n is equal to 
n * (n+1) / 2. The proof of this is that the average value is the series is (n+1)/2 and there are n elements.

So if we take the expected sum of all elements from 1 to n and subtract the actual sum, it will return the missing number from the series.
"""
class Solution:
    def solve(self, arr):
        n=len(arr)+1
        return n*(n+1)//2 - sum(arr)
