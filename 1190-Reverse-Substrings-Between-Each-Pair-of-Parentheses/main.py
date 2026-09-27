class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ')':
                reversed_chars = []

                while stack[-1] != '(':
                    reversed_chars.append(stack.pop())

                stack.pop() #this removes the (
                stack.extend(reversed_chars)
            else:
                stack.append(char)

        return "".join(stack)


if __name__ == '__main__':
    solution = Solution()
    result = solution.reverseParentheses(s = "(u(love)i)")
    print(result)