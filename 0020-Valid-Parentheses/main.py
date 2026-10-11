class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")" and (not stack or stack.pop() != "("):
                return False
            elif char == "]" and (not stack or stack.pop() != "["):
                return False
            elif char == "}" and (not stack or stack.pop() != "{"):
                return False
        return len(stack) == 0

if __name__ == '__main__':
    solution = Solution()
    result = solution.isValid(s = "()[]{}")
    print(result)