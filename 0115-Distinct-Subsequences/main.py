class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ways = [0] * (len(t) + 1)
        ways[0] = 1
        for char in s:
            for j in range(len(t) - 1, -1, -1):
                if char == t[j]:
                    ways[j + 1] += ways[j]
        return ways[-1]

if __name__ == '__main__':
    solution = Solution()
    result = solution.numDistinct(s = "rabbbit", t = "rabbit")
    print(result)