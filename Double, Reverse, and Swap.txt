"""
Double, Reverse, and Swap

The insight we need to solve this problem efficiently is to realise that each operation is independent. Reversing twice does nothing, even if the string was doubled or characters were swapped, and swapping characters twice does nothing even if the string is reversed or doubled. 

​

Therefore, we only need to check if the number of times we reverse is uneven and the number of times we swap is uneven, and do it once if so.

​

We also count the number of times we have to double with modulos and do it once with an exponential (bitshift could've been used also)

"""
class Solution:
    def solve(self, n):
        d={"x":"y", "y":"x"}
        s="xxy"
        dbl_count=(n+2)//3
        rev_count=(n+1)//3
        swap_count=(n)//3
        s *= 2 ** dbl_count
        if rev_count % 2 == 1:
            s = s[::-1]
        if swap_count % 2 == 1:
            s = "".join(d[c] for c in s)
        return s
