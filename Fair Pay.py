"""
Fair Pay

The key to this problem is to remember to iterate left-to-right and right-to-left. To illustrate the importance of this, let's take this test case:
[3,2,1,2,3]
If we only iterate left-to-right, we will never consider the strictly increasing sequence 3-2-1.
Probably possible in constant space with a stricly increasing counter, but that will be left as an exercice to the reader :).
"""
class Solution:
    def solve(self, ratings):
        pay=[1 for _ in ratings]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                pay[i] = pay[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                pay[i] = max(pay[i], pay[i+1]+1)
        return sum(pay)