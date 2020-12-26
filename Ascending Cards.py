"""
Ascending Cards

Same logic as crabmilk with minor optimizations. We apply the logic described in the problem using a double-ended queue, and map the cards to the resulting order. 

- Use a deque to be able to popleft() in constant time.
- Instead of sorting the order, you can make a buffer and assign the card at the correct position.
"""
from collections import deque
class Solution:
    def solve(self, cards):
        cards.sort()
        idx=[i for i in range(len(cards))]
        order=[]
        q=deque(idx)
        while q:
            order.append(q.popleft())
            if q: q.append(q.popleft())
        ans=[0 for _ in cards]
        for i,card in zip(order,cards):
            ans[i]=card
        return ans
