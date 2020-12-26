"""
24-Hour Time

Using Python's date time library, we can parse the string according to the specified format, and print it according to the required format.
"""
from datetime import datetime
class Solution:
    def solve(self, s):
        return datetime.strptime(s,"%I:%M%p").strftime("%H:%M")
