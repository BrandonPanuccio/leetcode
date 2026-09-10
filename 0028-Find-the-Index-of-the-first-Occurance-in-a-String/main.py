class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack)):
            if i+len(needle) <= len(haystack) and haystack[i:i+len(needle)] == needle:
                return i 
        return -1

if __name__ == '__main__':
    solution = Solution()
    result = solution.strStr("hello", "ll")
    print(result)