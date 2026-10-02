class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # if len(s) <= 1:
        #     return False

        hashlookup = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in ['(',"{","["]:
                stack.append(ch)
            elif (not stack) or (stack.pop() != hashlookup[ch]):
                return False
            
        if len(stack) == 0:
            return True
        return False
    

