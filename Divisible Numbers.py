"""
Divisible Numbers

Combination of the inclusion-exclusion principle and binary search:

We binary search between zero and n * max(a,b,c) for our answer. For each tested number, we count the number of multiples of that number using the inclusion-exclusion principle. If we don't have enough multiples for the current number, we search the higher bound otherwise we try to search lower.
"""
from math import gcd
class Solution:
    def solve(self, n, a, b, c):
        def lcm(a,b):
            return a*b // gcd(a,b)
            
        def count_multiples(x):
            ans = x // a + x // b + x // c
            ans -= x // lcm(a,b) + x // lcm(b,c) + x // lcm(a,c)
            ans += x // lcm(a,lcm(b,c))
            return ans
        lo = 0
        hi = n*max(a,b,c)
        ans=-1
        while lo <= hi:
            mid = (lo+hi)//2
            cnt = count_multiples(mid)
            print(mid,cnt)
            if cnt >= n:
                ans=mid
                hi = mid-1
            else:
                lo = mid+1
        return ans