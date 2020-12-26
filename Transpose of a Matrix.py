"""
Transpose of a Matrix

zip will pair corresponding elements together. For example:
```
[1,2,3]
[4,5,6]
```
will result in [(1,4), (2,5), (3,6)].  This is equivalent to a transposition.
```
[1,2,3]
[4,5,6]
[7,8,9]
=>
[(1,4,7),
 (2,5,8),
 (3,6,9)]
```
The star spreads the matrix and passes each list as an individual argument.
"""
class Solution:
    def solve(self, matrix):
        return list(zip(*matrix))
