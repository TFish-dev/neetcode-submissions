class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        
        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                
                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '-':
                    stack.append(a - b)
                elif tokens[i] == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(tokens[i])

        return int(stack[0])
