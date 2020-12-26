"""
2048

1. We rotate every direction to left to simplify procedure;
2. We eliminate 0 values to simply tracking neighbors;
3. We merge identical neighbors;
4. We pad with zeroes;
5. We restore original orientation.

(I called fn three times to restore 90 degrees rotation).
"""
class Solution:
    def solve(self, board, direction):
        fn=mapping[direction]
        return fn(fn(fn(fill(merge(fltr(fn(board)))))))
        
mapping = {
    "left": lambda lst: lst,
    "right": lambda lst: [l[::-1] for l in lst],
    "down": lambda lst: list(zip(*lst[::-1])),
    "up": lambda lst: list(zip(*lst))
}

def fltr(lst):
    return [[v for v in l if v != 0] for l in lst]

def merge(lst):
    for l in lst:
        i=0
        while i<len(l)-1:
            if l[i]==l[i+1]:
                l[i]*=2
                l.pop(i+1)
            i+=1
    return lst

def fill(lst):
    for i in range(len(lst)):
        while len(lst[i]) != 4: 
            lst[i].append(0)
    return lst