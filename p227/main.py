class Solution:

    def calculate(self, expr: str) -> int:
        def operate(a, op , b):
            if op == "+":
                return a+b
            elif op == "-":
                return a-b
            elif op == "*":
                return a*b
            elif op == "/":
                return a//b
        priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }
        expr = expr.replace(" ", "")
        getNum = 0
        numStack = []
        opStack = []
        
        i = 0

        while i <= len(expr):
            if i<len(expr) and expr[i].isdigit():
                getNum = getNum*10+int(expr[i])
            else:
                numStack.append(getNum)
                getNum = 0
                    
                if len(opStack)>0 and (i>=len(expr) or priority[opStack[-1]] >= priority[expr[i]]):
                    while len(opStack)>0:
                        b = numStack.pop()
                        a = numStack.pop()
                        op = opStack.pop()
                        numStack.append(operate(a, op , b))
                
                if i<len(expr):
                    opStack.append(expr[i])
            i = i + 1
        return numStack[-1]
                
s = Solution()
print(s.calculate("0"))
print(s.calculate("1+2*5/3+6/4*2"))
print(s.calculate("3+2*2"))
print(s.calculate(" 3/2 "))
print(s.calculate(" 3+5 / 2 "))
print(s.calculate("1+1+1"))
print(s.calculate("2-3+4"))
print(s.calculate("1*2-3/4+5*6-7*8+9/10"))

