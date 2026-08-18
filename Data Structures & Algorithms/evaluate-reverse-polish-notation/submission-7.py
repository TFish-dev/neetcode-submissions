class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["-","+","*","/"]

        for i in range(len(tokens)):
            if tokens[i] in ops:
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(a + b)
                elif tokens[i] == "-":
                    stack.append(b - a)
                elif tokens[i] == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
            else:
                stack.append(tokens[i])
        
        return int(stack[0])