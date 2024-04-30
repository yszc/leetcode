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
        numStack = [0]
        opStack = []

        for c in expr:
            if c.isdigit():
                getNum = getNum*10+int(c)
            else:
                numStack.append(getNum)
                getNum = 0
                
                while len(opStack)>0 and priority[opStack[-1]]>=priority[c]:
                    b = numStack.pop()
                    a = numStack.pop()
                    op = opStack.pop()
                    numStack.append(operate(a, op , b))
                opStack.append(c)

                
                    
        numStack.append(getNum)
        while len(opStack)>0:
            b = numStack.pop()
            a = numStack.pop()
            op = opStack.pop()
            numStack.append(operate(a, op , b))
        return numStack[-1]

s = Solution()
print(s.calculate("3+2*2"))
print(s.calculate(" 3/2 "))
print(s.calculate(" 3+5 / 2 "))
print(s.calculate("1+1+1"))
print(s.calculate("2-3+4"))
print(s.calculate("1*2-3/4+5*6-7*8+9/10"))

