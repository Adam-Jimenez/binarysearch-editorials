"""
Rocketship Rescue

Each iteration, we put the fattest dude on the ship. Then we check the lightest. If he can't go on the ship, then we know that no other person can because they're all fatter. 
"""
class Solution:
    def solve(self, weights, limit):
        weights.sort()
        cnt=0
        while weights:
            x=weights.pop()
            if weights and weights[0]<=limit-x:
                weights.pop(0)
            cnt+=1
        return cnt
                
