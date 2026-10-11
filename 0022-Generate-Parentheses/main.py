class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp = {0: [""]}
        for pairs in range(1, n + 1):
            dp[pairs] = []
            for inside_pairs in range(pairs):
                after_pairs = pairs - 1 - inside_pairs
                for inside in dp[inside_pairs]:
                    for after in dp[after_pairs]:
                        dp[pairs].append("(" + inside + ")" + after)
        return dp[n]

if __name__ == '__main__':
    solution = Solution()
    result = solution.generateParenthesis(n = 3)
    print(result)