"""
Foo Bar Qaz Qux

LOOK AT OTHER EDITORIAL
Three cases:
If there is only one unique color: return the length of the string.

Now it gets funky. If the frequency are all even or all odd, the answer will be two. Here's my best explanation as to why. At each iteration, we remove one from the frequency of two colors, and add one to the frequency of the last color. Here's an illustration, where R and G are combined.
```
R G B
4 4 4
3 3 5
```
If we remove one from an even number, it will give an odd number. The same holds when we add one to an even number. So if all frequencies are even on one iteration, they will all be odd on the next, and then even, etc. Following this line of logic, the frequency of each color will eventually be (1,1,1):
```
R G B
4 4 4
3 3 5
2 2 6
1 1 7
2 0 6
1 1 5
2 0 4
1 1 3
2 0 2
1 1 1
```
And when that happens, we are fucked. Because when we combine two of those colors, we will be left with two identical colors.

Here's what happens if they are not all even or odd:
```
R G B
3 4 4
2 3 5
1 2 6
0 1 7
1 0 6
0 1 5
1 0 4
0 1 3
1 0 2
0 1 1
```
In the final state, one or two numbers will be even, and the rest one will be odd. If two ones are left, we can make our last one, otherwise we already reached our end state.
"""
from collections import Counter
class Solution:
    def solve(self, quxes):
        cnt=Counter(quxes)
        if len(cnt)==1: return len(quxes)
        if len({x%2 for x in cnt.values()}) == 1: return 2
        return 1