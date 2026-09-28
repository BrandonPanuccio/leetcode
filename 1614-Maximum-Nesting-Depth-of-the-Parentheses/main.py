class Solution:
    def maxDepth(self, s: str) -> int:
        maximum_depth=0
        counter = 0
        for char in s:
            if char == '(':
                counter += 1
            if char == ')':
                maximum_depth = max(maximum_depth, counter)
                counter -= 1

        return maximum_depth

if __name__ == '__main__':
    solution = Solution()
    result = solution.maxDepth(s = "(1)+((2))+(((3)))")
    print(result)