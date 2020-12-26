"""
List Calculator

Don't waste your time, let python eval shit for you

"""
class Solution:
    def solve(self, nums, op, val):
        op = "//" if op == "/" else op
        return list(map(lambda x: eval(op.join([str(x),str(val)])),nums))
        