"""
Postfix Notation Evaluation

We traverse each element and push it onto a stack. Each time we meet an operator, we apply it to the last two elements pushed onto the stack. 
"""
from operator import add,sub,mul
fn={
"+": add,
"-": sub,
"*": mul,
"/": lambda x,y: int(x/y)
}
class Solution:
    def solve(self, exp):
        stk=[]
        for x in exp:
            if x in fn:
                a,b=stk.pop(), stk.pop()
                stk.append(fn[x](b,a))
            else:
                stk.append(int(x))
        return stk[0]
    
