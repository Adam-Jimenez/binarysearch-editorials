"""
Justify Text

First step: 
Take as many words as you can on a line. The formula for this is this: the length of all the words + the length of the next word + the space in between (the length of the line) must be less or equal to k.
Second step:
Compute the remaining space by subtracting the total length from words from k. If there is one word append the space to it. If there are many words, divide the remaining space in len(line)-1, the number of spaces between words. Take the remainder and sequentially add it to words starting from the start.
"""
class Solution:
    def solve(self, words, k):
        ans=[]
        i=0
        while i<len(words):
            line=[]
            while i<len(words) and (sum(map(len,line)) + len(line) + len(words[i])) <= k:
                line.append(words[i])
                i+=1
            remaining_space = k-sum(map(len,line))
            if len(line) == 1:
                line[0]+=" "*remaining_space
                ans.append(line[0])
            else:
                space_len,space_rem = divmod(remaining_space,len(line)-1)
                for j in range(space_rem):
                    line[j] += " "
                ans.append((" "*space_len).join(line))
        return ans
            