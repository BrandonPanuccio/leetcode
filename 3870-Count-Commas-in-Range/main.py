class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        return n - 999
        
if __name__ == '__main__':
    solution = Solution()
    result = solution.countCommas(n=1002)
    print(result)