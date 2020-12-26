"""
Number of Quadruplets That Sum Target

We compute all sums between a&b and c&d and count their frequencies. For each sum in s1, we add its frequency times the frequency of its complement in s2, which gives the number of possible unique combinations.
"""
from collections import Counter
class Solution:
    def solve(self, a, b, c, d, target):
        s1 = Counter([a[i]+b[j] for i in range(len(a)) for j in range(len(b))])
        s2 = Counter([c[i]+d[j] for i in range(len(c)) for j in range(len(d))])
        ans=0
        for k,v in s1.items():
            ans+=v*s2[target-k]
        return ans
