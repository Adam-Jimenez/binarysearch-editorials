"""
Moo

I hold a dictionary for every cow and their direction. Then i iterate over each cow, and try to move it to the next position. If two cows reserve the same position, none goes there. When no change is made, we return the result.
"""
class Solution:
    def solve(self, cows):
        cow_line=[c for c in cows]
        cow_directions={}
        for i,c in enumerate(cow_line):
            if c=="L" or c=="R":
                cow_directions[i] = cow_to_direction(c)
        done=False
        while not done:
            done=True
            mark=[None for _ in cow_line]
            for pos,dir in cow_directions.items():
                if 0<=pos+dir<len(cow_line) and cow_line[pos+dir]=="@":
                    if mark[pos+dir] is None:
                        mark[pos+dir] = cow_line[pos]
                    else:
                        mark[pos+dir] = None
            cow_directions={}
            for i,cow in enumerate(mark):
                if cow is not None:
                    done=False
                    cow_line[i]=cow
                    cow_directions[i]= cow_to_direction(cow)
        return "".join(cow_line)

def cow_to_direction(cow):
    return 1 if cow=="R" else -1