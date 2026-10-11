class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0
        for i, num in enumerate(nums):
            if n % (i+1) == 0:
                result += num**2
        return result

if __name__ == '__main__':
    solution = Solution()
    result = solution.sumOfSquares(nums = [2,7,1,19,18,3])
    print(result)