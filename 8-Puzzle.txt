"""
8-Puzzle

A* solution.

First we can check if the problem is solvable with the trick described here: https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/.

Then we use our A* path finding algorithm, using the number of misplaced numbers as an heuristic.
"""
from heapq import heappush, heappop
class Solution:
    def solve(self, board):
        board = tuple([x for r in board for x in r])
        target = tuple(range(9))
        if inversions(board)&1: return -1
        d=dist(board)
        q=[(d,0,board)]
        seen=set()
        while q:
            cost,swaps,state =heappop(q)
            if state==target: return swaps
            if state in seen: continue
            seen.add(state)
            for next_state in get_neighbors(state):
                heappush(q,(dist(next_state)+swaps+1,swaps+1,next_state))

def inversions(board):
    sm=0
    for i in range(len(board)):
        if not board[i]: continue
        for j in range(i+1, len(board)):
            if not board[j] : continue
            if board[i]>board[j]:
                sm+=1
    return sm
    
def dist(board):
    return sum(1 for i,x in enumerate(board) if x!=0 and i!=x)

def get_neighbors(board):
    board=list(board)
    i = board.index(0)
    if i % 3 > 0:
        board[i], board[i-1] = board[i-1], board[i]
        yield tuple(board)
        board[i], board[i-1] = board[i-1], board[i]
    if i % 3 < 2:
        board[i], board[i+1] = board[i+1], board[i]
        yield tuple(board)
        board[i], board[i+1] = board[i+1], board[i]
    if i//3 > 0:
        board[i], board[i-3] = board[i-3], board[i]
        yield tuple(board)
        board[i], board[i-3] = board[i-3], board[i]
    if i//3 < 2:
        board[i], board[i+3] = board[i+3], board[i]
        yield tuple(board)
        board[i], board[i+3] = board[i+3], board[i]
