class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        next_comma = 1000
        while n >= next_comma:
            total += n - next_comma + 1
            next_comma *= 1000

        return total

if __name__ == '__main__':
    solution = Solution()
    result = solution.countCommas(104521)
    print(result)