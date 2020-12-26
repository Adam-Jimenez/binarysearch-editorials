"""
CCCXXVV

Hack-ish solution, but since there's a small number of numbers where the prefix is smaller, you can just enumerate them. 

Also, dictionaries are not ordered, so if single-letter roman numbers are iterated through first, this wouldn't work. 
"""
d={
    'CM': 900,
    'XL': 40,
    'IX': 9,
    'IV': 4,
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
class Solution:
    def solve(self, numeral):
        a=0
        for k,v in d.items():
            a+=numeral.count(k)*v
            numeral=numeral.replace(k,"")
        return a
