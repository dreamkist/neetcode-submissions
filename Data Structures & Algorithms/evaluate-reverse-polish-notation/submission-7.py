from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            match i:
                case '+':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 + num1)
                case '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 - num1)
                case '*':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 * num1)
                case '/':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num2 / num1))
                case _:
                    stack.append(int(i))
        return stack[-1]