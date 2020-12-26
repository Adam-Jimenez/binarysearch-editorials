"""
Add Binary Numbers

You can parse the binary string with the int constructor. The second parameter specifies the base. Then we reconvert the result to binary, and remove the prefix "0b".
"""
class Solution:
    def solve(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]
