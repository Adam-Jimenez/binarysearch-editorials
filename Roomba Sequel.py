"""
Roomba Sequel

No tricks here, just implement what is told. Here is a clean example, with a dictionary of functions to apply the moves.
"""
move={
    "NORTH": lambda x,y: (x,y+1),
    "EAST": lambda x,y: (x+1,y),
    "SOUTH": lambda x,y: (x,y-1),
    "WEST": lambda x,y: (x-1,y)
}
class Solution:
    def solve(self, moves, tx, ty):
        x,y=0,0
        seen={(x,y)}
        for m in moves:
            while (x,y) in seen:
                x,y = move[m](x,y)
            seen.add((x,y))
        return (x,y)==(tx,ty)