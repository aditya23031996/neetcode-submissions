class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {"[":"]", "(":")", "{":"}"}

        for char in s:
            if char in parenthesis:
                stack.append(parenthesis[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        return len(stack) == 0