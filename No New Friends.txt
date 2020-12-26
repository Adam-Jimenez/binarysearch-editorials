"""
No New Friends

Two solutions:

- Build a set from all people in friendships and check its length is n
- Check all people (x) in range(n) is in any friendship
"""
class Solution:
    def solve(self, n, friends):
        # Efficient version
        
        # return len(set(person for group in friends for person in group)) == n
        
        # Simple version
        return all(any(x in f for f in friends) for x in range(n))
