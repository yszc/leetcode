class Solution:

    def tokenizer(self, expr: str):
        """
        词法分析
        """
        expr = expr.replace(" ", "")
        tokens = []
        for c in expr:
            if c.isdigit():
                if tokens and tokens[-1].isdigit():
                    tokens[-1] += c
                else:
                    tokens.append(c)
            else:
                tokens.append(c)

        tokens.append(';')
        return tokens 
    
    def analyzer(self, tokens):
        """
        语法分析： BNF表达式
        expression = term {+ term |- term}
        term = factor{* factor| / factor}
        factor = NUM | ( expression )
        """
        def operate(a, op , b):
            if op == "+":
                return a+b
            elif op == "-":
                return a-b
            elif op == "*":
                return a*b
            elif op == "/":
                return a//b

        tnum = 0
        def newtemp():
            nonlocal tnum
            tnum += 1
            return "t%d" % (tnum)
        def expression(i):
            i, a = term(i)
            while(tokens[i] in ["+","-"]):
                op = tokens[i]
                i += 1
                i, b = term(i)
                # a = operate(a, op , b)
                tp = newtemp()
                print(tp, a, op , b)
                a = tp
            return i, a
        def term(i):
            i, a = factor(i)
            while(tokens[i] in ["*","/"]):
                op = tokens[i]
                i += 1
                i, b = term(i)
                # a = operate(a, op , b)
                tp = newtemp()
                print(tp, a, op , b)
                a = tp
            return i, a
                
        def factor(i):
            if tokens[i].isdigit():
                return i+1, int(tokens[i])
            elif tokens[i] == "(":
                i += 1
                i, a = expression(i)
                if tokens[i] == ")":
                    i += 1
                    return i, a
                else:
                    raise Exception("SyntaxError")
            else:
                raise Exception("SyntaxError")
        
        i,res = expression(0)
        if tokens[i] != ";":
            raise Exception("SyntaxError")
        return res

    def calculate(self, expr: str) -> int:
        tokens = self.tokenizer(expr)
        return self.analyzer(tokens)

s = Solution()
print(s.calculate("2+3*4"))
print(s.calculate("(2+3)/4"))
print(s.calculate("14/3*2"))

# print(s.calculate("0"))
# print(s.calculate("1+2*5/3+6/4*2"))
# print(s.calculate("3+2*2"))
# print(s.calculate(" 3/2 "))
# print(s.calculate(" 3+5 / 2 "))
# print(s.calculate("1+1+1"))
# print(s.calculate("2-3+4"))
# print(s.calculate("1*2-3/4+5*6-7*8+9/10"))
# print(s.calculate("100+200/4*3-50"))

