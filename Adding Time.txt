"""
Adding Time

Built-in solutions baby! Using Python's datetime package, you can specify the format of the string and modify it to your will.
"""
from datetime import datetime, timedelta
format="%I:%M%p"
class Solution:
    def solve(self, s, n):
        return (datetime.strptime(s,format)+timedelta(minutes=n)).strftime(format).lower()
