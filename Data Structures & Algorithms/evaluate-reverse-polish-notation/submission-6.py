class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["-","+","*","/"]

        for i in range(len(tokens)):
            if tokens[i] in ops:
                if tokens[i] == "+":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a + b)
                elif tokens[i] == "-":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b - a)
                elif tokens[i] == "*":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a * b)
                else:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(b / a))
            else:
                stack.append(tokens[i])
        
        return int(stack[0])