"""
String Clockwise Shift

(ord(c2)-ord(c1))%26 will automatically compute the right shift needed, as long as your language supports negative modulos.
We check if the sum of the necessary shifts are smaller than k.
"""
class Solution:
    def solve(self, a, b, k):
        return k>=sum((ord(c2)-ord(c1))%26 for c1,c2 in zip(a,b))
        
