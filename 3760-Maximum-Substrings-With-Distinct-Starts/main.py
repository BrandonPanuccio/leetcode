class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))

if __name__ == '__main__':
    solution = Solution()
    result = solution.maxDistinct("abab")
    print(result)