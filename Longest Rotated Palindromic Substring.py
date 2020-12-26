"""
Longest Rotated Palindromic Substring

How I Learned to Stop Worrying and Love the Palindrome.

Here's a cool trick to check for substring palindromes.

Let's take a palindrome s="racecar".

and two pointers, i=4 and j=4, that denote the middle of a potential palindrome.

As long as the two characters s[i] and s[j] are equal, we can decrement i and increment j to find the length. Example:

palindrome\_len = 0

"r a c e c a r"

i .......^.........

j........^.........

s[i] == s[j] ? yes: palindrome += 1 if i == j else 2

palindrome\_len = 1

"r a c e c a r"

i .....^..........

j ...........^....

s[i] == s[j] ? yes: palindrome += 1 if i == j else 2

palindrome\_len = 3

"r a c e c a r"

i ..^..............

j ..............^..

s[i] == s[j] ? yes: palindrome += 1 if i == j else 2

palindrome\_len = 5

"r a c e c a r"

i ^.................

j .................^

s[i] == s[j] ? yes: palindrome += 1 if i == j else 2

palindrome\_len = 7

We stop iterating if the palindrome length matches the string length.

This also works for even-length palindromes, such as s="anna".

Instead of having i and j start at the same value, we increment j.

"a n n a"

i ..^......

j......^...

And repeat the same process as before.

Now, we can iterate over every index in s, and look for the longest palindrome at that position. To deal with the rotation, we just have to use modulos each time we increment and decrement the pointers. In Python, -1 % len(s) will give len(s)-1, so we will loop around the string automatically.

​

​

​

​

"""
class Solution:
    def solve(self, s):
        maxx=0
        for i in range(len(s)):
            maxx=max(maxx, longest(s, i, i))
            maxx=max(maxx, longest(s, i, i+1))
            print(i, maxx)
        return maxx
        # Write your code here
    
def longest(s, i, j):
    l=0
    i = i%len(s)
    j = j%len(s)
    while(s[i]==s[j] and l<=len(s)):
        if l==0 and i == j:
            l+=1
        elif i != j:
            l+=2
        else:
            break
        i-=1
        j+=1
        i = i%len(s)
        j = j%len(s)
    return min(l, len(s))
